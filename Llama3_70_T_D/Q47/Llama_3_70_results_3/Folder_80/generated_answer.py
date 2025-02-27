def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[35:89]
    result = set()
    for length in range(24, 34):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result