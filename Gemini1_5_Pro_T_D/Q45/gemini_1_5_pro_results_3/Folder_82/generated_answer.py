from itertools import permutations

def palindromes_between_indices(text):
    letters = set()
    for i in range(1, 7):
        if text[i].isalpha():
            letters.add(text[i].lower())
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes