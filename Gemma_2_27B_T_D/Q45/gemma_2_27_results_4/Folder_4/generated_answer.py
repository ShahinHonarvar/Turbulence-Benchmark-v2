from itertools import permutations

def palindromes_between_indices(text):
    chars = ''.join([c for c in text[3:10] if c.isalpha()])
    palindromes = set()
    for p in permutations(chars):
        word = ''.join(p)
        if len(word) >= 7 and word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes