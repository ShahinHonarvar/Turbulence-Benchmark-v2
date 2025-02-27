from itertools import permutations

def palindromes_between_indices(text):
    Letters = text[1:6].lower()
    palindromes = set()
    for p in permutations(Letters):
        word = ''.join(p)
        if word[::-1] == word and len(word) >= 6:
            palindromes.add(word)
    return palindromes