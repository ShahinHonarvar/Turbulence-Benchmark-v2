def palindromes_between_indices(s):
    s = s.upper()
    ans = set()
    for i in range(1, 7):
        for j in range(i, 8):
            for perm in itertools.permutations(s[i:j + 1]):
                ans.add(''.join(perm))
    return ans