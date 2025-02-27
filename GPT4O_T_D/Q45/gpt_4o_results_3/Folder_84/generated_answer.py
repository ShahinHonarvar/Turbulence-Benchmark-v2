from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        for i in range(3, len(letters) + 1):
            for j in range(len(perm) - i + 1):
                sub = perm[j:j + i]
                if sub == sub[::-1]:
                    palindromes.add(''.join(sub))
    return palindromes