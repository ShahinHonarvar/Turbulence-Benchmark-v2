def palindromes_between_indices(s):
    s = s[1:5]
    letters = set()
    for i in s:
        letters.add(i.lower())
    palindromes_set = set()
    for i in range(5, len(s) + 1):
        for p in permutations(letters, i):
            p = ''.join(p)
            if p == p[::-1] and len(p) >= 5:
                palindromes_set.add(p)
    if len(palindromes_set) == 0:
        return set()
    else:
        return palindromes_set