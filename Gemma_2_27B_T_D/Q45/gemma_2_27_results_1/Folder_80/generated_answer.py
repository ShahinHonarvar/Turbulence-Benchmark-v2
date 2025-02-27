from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([c for c in text[3:9] if c.isalpha()])
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 7 and word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes