from itertools import permutations

def palindromes_between_indices(text):
    letters = sorted([letter for letter in text[4:10] if letter.isalpha()])
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 5 and word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes