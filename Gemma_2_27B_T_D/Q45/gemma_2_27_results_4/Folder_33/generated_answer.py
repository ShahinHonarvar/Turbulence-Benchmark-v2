from itertools import permutations

def palindromes_between_indices(text):
    letters = ''
    for i in range(7, 10):
        if i < len(text) and text[i].isalpha():
            letters += text[i].lower()
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes