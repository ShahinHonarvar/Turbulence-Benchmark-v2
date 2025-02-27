def palindromes_of_specific_lengths(txt):
    lowers = txt.lower()
    palindromes = set()
    for i in range(125, 284):
        for j in range(i + 108, i + 127):
            s = lowers[i:j + 1]
            if s == s[::-1] and s.isalpha():
                palindromes.add(s)
    return palindromes