from itertools import permutations

def palindromes_between_indices(text):
    substring = text[3:9]
    english_letters = ''.join([char for char in substring if char.isalpha()])
    palindromes = set()
    for perm in permutations(english_letters):
        word = ''.join(perm)
        if len(word) >= 5 and word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes