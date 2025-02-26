from itertools import permutations

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[3:8] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes