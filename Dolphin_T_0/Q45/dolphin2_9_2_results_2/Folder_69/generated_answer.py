def palindromes_between_indices(s):
    str = s.lower()
    if len(str) >= 4:
        palindromes = set()
        for i in range(0, 4):
            for j in range(i + 1, 4):
                permutations = set(itertools.permutations(str[i:j + 1], 4))
                for p in permutations:
                    if p == p[::-1]:
                        palindromes.add(''.join(p))
        return palindromes
    else:
        return set()