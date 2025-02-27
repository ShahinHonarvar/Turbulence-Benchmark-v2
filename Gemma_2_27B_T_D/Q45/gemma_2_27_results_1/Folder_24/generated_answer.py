from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[2:10])).lower()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes