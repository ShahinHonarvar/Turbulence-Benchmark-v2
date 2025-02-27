from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(lambda c: c.isalpha(), text[5:10])).lower()
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes