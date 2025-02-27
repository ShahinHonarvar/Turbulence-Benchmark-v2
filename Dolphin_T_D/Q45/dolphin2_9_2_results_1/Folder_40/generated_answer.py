def palindromes_between_indices(s):
    s = s[4:10]
    s = ''.join([i.lower() for i in s if i.isalpha()])
    length = 7
    return set([''.join(p) for p in permutations(s) if p == p[::-1] and len(p) >= length])