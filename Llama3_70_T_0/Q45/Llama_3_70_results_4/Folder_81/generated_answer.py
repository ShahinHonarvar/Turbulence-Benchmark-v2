from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            for p in permutations(letters[i:i + length]):
                w = ''.join(p)
                if w == w[::-1]:
                    palindromes.add(w)
    return palindromes