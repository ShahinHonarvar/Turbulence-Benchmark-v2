import itertools

def palindromes_between_indices(s):
    s = s[4:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            word = ''.join(combo)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes