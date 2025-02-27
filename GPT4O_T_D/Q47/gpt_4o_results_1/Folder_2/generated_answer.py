def palindromes_of_specific_lengths(s):
    s = s[10:60]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    palindromes = set()
    for start in range(n):
        for length in range(18, 37):
            end = start + length
            if end <= n:
                substring = s[start:end]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes