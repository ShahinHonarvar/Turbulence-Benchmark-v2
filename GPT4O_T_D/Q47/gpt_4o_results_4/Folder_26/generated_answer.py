def palindromes_of_specific_lengths(s):
    s = s[24:85]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for l in range(21, 32):
        for i in range(n - l + 1):
            sub = s[i:i + l]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes