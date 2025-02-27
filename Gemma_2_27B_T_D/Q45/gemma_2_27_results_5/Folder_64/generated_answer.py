from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[4:10] if c.isalpha()]
    palindromes = set()
    for permutation in permutations(letters):
        word = ''.join(permutation)
        if len(word) >= 5 and word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes