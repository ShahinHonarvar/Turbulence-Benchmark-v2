def palindromes_of_specific_lengths(s):
    s = s[13:90]
    result = set()
    for length in range(55, 72):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub.lower()[::-1]:
                result.add(sub)
    return result