import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:6] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            word = ''.join(combo)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes