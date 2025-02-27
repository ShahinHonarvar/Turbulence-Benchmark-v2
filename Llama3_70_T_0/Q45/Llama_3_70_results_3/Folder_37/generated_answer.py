from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        for i in range(len(p)):
            for j in range(i + 5, len(p) + 1):
                sub = ''.join(p[i:j])
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes