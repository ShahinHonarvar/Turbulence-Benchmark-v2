def palindromes_of_specific_lengths(s):
    s = s[26:91]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for start in range(len(s)):
        for length in range(27, 59):
            if start + length <= len(s):
                substring = s[start:start + length]
                if substring == substring[::-1]:
                    result.add(substring)
    return result