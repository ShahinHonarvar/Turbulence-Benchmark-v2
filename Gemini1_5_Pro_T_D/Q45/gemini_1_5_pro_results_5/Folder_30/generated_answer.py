from itertools import permutations

def palindromes_between_indices(text):
    letters = set()
    for i in range(5):
        if text[i].isalpha():
            letters.add(text[i].lower())
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for item in permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)
    return palindromes