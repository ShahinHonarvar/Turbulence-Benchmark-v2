from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:6] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, len(letters) // 2):
        word = ''.join(p + p[-(len(p) - 1)::-1])
        palindromes.add(word.lower())
    return palindromes