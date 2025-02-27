import itertools

def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[5:8] if c.isalpha()))
    result = set()
    for length in range(4, len(letters) + 1):
        for p in itertools.permutations(letters, length):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result