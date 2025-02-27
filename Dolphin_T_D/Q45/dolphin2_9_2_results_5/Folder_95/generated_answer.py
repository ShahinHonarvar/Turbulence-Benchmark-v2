def palindromes_between_indices(s):
    letters = s[7:9]
    palindromes = {''}
    for _ in range(3, len(letters) + 1):
        palindromes |= set([p + l + p[::-1] for p in palindromes for l in letters])
    return palindromes