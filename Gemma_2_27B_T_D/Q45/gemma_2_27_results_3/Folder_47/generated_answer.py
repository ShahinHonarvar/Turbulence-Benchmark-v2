from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([char for char in text[3:8] if char.isalpha()])
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 5 and word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes