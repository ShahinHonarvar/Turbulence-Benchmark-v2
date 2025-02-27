import itertools

def palindromes_between_indices(s):
    s = s.lower()
    chars = [c for c in s[2:5] if c.isalpha()]
    if len(chars) < 3:
        return set()
    palindromes = set()
    for r in range(3, len(chars) + 1):
        for perm in itertools.permutations(chars, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes