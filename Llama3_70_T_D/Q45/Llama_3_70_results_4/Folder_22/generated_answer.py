import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[5:7] if char.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes