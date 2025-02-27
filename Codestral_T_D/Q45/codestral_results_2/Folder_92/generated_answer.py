from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:8].lower()
    palindromes = set()
    for p in permutations(s):
        for i in range(3, len(p) + 1):
            sub = p[:i]
            if sub == sub[::-1]:
                palindromes.add(''.join(sub))
    return palindromes