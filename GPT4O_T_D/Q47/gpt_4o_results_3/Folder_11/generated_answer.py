def palindromes_of_specific_lengths(s):
    s = s[24:98]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(10, 37):
            end = start + length
            if end <= len(s):
                substring = s[start:end]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes