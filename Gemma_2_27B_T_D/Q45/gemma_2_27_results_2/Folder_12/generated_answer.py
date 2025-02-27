def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:9])).lower()
    return {''.join(p) for p in (perms for i in range(len(letters), 3, -1) for perms in (p for p in permutations(letters, i) if p == p[::-1]))}