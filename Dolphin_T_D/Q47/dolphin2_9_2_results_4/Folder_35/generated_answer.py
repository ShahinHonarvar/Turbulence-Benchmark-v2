def palindromes_of_specific_lengths(s):
    result = set()
    s = s[34:91]
    for length in range(14, 40):
        for i in range(len(s) - length + 1):
            subset = s[i:i + length]
            if subset == subset[::-1]:
                result.add(subset)
    return result