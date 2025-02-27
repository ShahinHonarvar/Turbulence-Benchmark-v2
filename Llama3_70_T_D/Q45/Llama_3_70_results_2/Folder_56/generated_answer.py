from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[5:10] if char.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes