def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 61):
        for j in range(i + 62, len(s) + 1):
            subsetting = s[i:j]
            if len(subsetting) >= 62:
                if set(subsetting) <= set('abcdefghijklmnopqrstuvwxyz'):
                    if subsetting == subsetting[::-1]:
                        palindromes.add(subsetting)
    return palindromes