def palindromes_of_specific_lengths(s):
    s = s[10:75]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for start in range(len(s)):
        for length in range(6, 9):
            end = start + length
            if end <= len(s):
                substring = s[start:end]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes