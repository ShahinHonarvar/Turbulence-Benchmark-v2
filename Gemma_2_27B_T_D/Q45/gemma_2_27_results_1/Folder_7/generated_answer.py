from itertools import permutations

def palindromes_between_indices(text):
    letters = text[1:10]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if len(word) >= 7 and word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes