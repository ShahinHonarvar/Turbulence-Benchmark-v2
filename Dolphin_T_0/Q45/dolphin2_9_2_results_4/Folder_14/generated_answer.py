def palindromes_between_indices(s):
    sub = s[4:6].lower()
    letters = ''.join(sorted(sub))
    n = len(letters)
    if n < 3:
        return set()
    palindromes = set()
    for p in range(n):
        for q in range(p, n):
            if letters[p:q + 1] != letters[p:q + 1][::-1]:
                continue
            palindromes.add(letters[p:q + 1])
    return palindromes