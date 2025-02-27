def palindromes_between_indices(s) -> set:
    s = s[0:6].lower()
    letters = set(s)
    palindromes = set()
    if len(s) < 3:
        return palindromes
    for i in range(3, len(s) + 1):
        for d in combinations_with_replacement(letters, i):
            if d == d[::-1]:
                palindromes.add(''.join(d))
    return palindromes