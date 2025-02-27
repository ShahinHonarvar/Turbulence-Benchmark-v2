def palindromes_of_specific_lengths(s):
    s = s[15:78].lower()
    lengths = range(43, 48)
    palindromes = set()
    for l in lengths:
        for i in range(len(s) - l + 1):
            sub = s[i:i + l]
            if sub == sub[::-1] and all((c.isalpha() for c in sub)):
                palindromes.add(sub)
    return palindromes