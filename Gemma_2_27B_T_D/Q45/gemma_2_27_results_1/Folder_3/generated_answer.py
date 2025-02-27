from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(text[7:10]).lower()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes