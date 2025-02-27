from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:10] if c.isalpha()))
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if len(word) >= 6 and word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes