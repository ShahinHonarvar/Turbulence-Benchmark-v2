from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([char for char in text[5:10] if char.isalpha()]).lower()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes