from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([letter for letter in text[3:10] if letter.isalpha()])
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes