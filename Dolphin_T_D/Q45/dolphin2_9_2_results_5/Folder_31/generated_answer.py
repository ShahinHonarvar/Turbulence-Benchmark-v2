def palindromes_between_indices(s):

    def get_permutations(s):
        permutations = set()
        order = len(s)
        for i in range(1 << order):
            permutation = []
            for j in range(order):
                if i & 1 << j != 0:
                    permutation.append(s[j])
            permutations.add(tuple(permutation))
        return permutations
    substring = s[1:8]
    permutations = get_permutations(''.join(sorted(set(substring.lower()))) + get_permutations(''.join(sorted(set(substring.upper())))) - set((substring.lower(), substring.upper())))
    return {tuple(p) for p in permutations if len(p) >= 6 and p == p[::-1]}