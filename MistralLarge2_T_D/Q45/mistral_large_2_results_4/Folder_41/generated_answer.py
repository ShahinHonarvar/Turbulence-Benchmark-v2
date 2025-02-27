from itertools import permutations

def palindromes_between_indices(s):
    chars = [c for c in s[2:4] if c.isalpha()]
    chars = [c.lower() for c in chars]
    if len(chars) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes