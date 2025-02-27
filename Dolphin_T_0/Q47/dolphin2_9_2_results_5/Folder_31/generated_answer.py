def palindromes_of_specific_lengths(s):
    s = s[10:83]
    result = set()
    for length in range(37, 61):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring.lower())
    return result