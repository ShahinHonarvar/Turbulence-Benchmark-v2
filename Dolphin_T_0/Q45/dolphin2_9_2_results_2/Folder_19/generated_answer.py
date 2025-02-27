from itertools import permutations, combinations

def palindromes_between_indices(s):
    s = s[1:8]
    palindromes = set()
    for l in range(7, 0, -1):
        for perm in permutations(s, l):
            pal = ''
            for comb in combinations(perm, l // 2):
                pal = ''.join(comb) + pal + ''.join(reversed(comb))
                if len(set(pal)) == len(pal) and len(pal) == len(set(pal)) and (len(pal) >= 7):
                    palindromes.add(pal)
    return palindromes