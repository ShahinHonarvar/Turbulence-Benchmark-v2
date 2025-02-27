def palindromes_of_specific_lengths(s):
    s = s[43:96].lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(18, 48):
            end = start + length
            if end <= len(s):
                substring = s[start:end]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes