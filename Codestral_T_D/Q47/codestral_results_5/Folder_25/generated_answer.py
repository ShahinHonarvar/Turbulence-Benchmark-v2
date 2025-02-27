def palindromes_of_specific_lengths(s):
    s = s[26:85]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for l in range(30, 47):
        for i in range(len(s) - l + 1):
            sub = s[i:i + l]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes