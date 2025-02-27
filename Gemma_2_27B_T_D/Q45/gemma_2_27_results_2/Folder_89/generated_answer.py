from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[5:10])).lower()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes