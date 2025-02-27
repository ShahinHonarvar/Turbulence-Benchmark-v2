def palindromes_of_specific_lengths(s):
    s = s[2:9].lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(3, 5):
            end = start + length
            if end <= len(s):
                substring = s[start:end]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes