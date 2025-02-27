def palindromes_of_specific_lengths(s):
    s = s[15:95]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(18, 74):
            if start + length <= len(s):
                substring = s[start:start + length]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes