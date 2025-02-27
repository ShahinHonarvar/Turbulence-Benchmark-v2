from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:6].lower()
    palindromes = set()
    for p in permutations(s):
        if len(p) >= 6:
            for i in range(len(p) // 2):
                if p[i] != p[-(i + 1)]:
                    break
            else:
                palindromes.add(''.join(p))
    return palindromes