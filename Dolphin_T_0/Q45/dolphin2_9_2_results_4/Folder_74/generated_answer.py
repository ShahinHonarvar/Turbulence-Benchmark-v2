def palindromes_between_indices(s):
    letters = set(s[1:7].lower())
    length = 6
    while length <= len(s[1:7]):
        for p in (''.join(p) for p in permutations(letters, length)):
            if p == p[::-1]:
                return set(p)
        length += 1
    return set()