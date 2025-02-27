from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(text[1:9].lower())
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes