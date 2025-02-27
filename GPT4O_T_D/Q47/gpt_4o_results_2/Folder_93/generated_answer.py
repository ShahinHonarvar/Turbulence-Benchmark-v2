def palindromes_of_specific_lengths(s):
    result = set()
    s = s[17:96]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    for length in range(13, 50):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result