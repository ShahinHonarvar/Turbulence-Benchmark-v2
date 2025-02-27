def palindromes_of_specific_lengths(s):
    s = s[:11]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for start in range(len(s)):
        for length in range(3, 6):
            if start + length <= len(s):
                substring = s[start:start + length]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes