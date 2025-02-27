import itertools

def palindromes_between_indices(text):
    letters = set()
    for i in range(5, 9):
        if text[i].isalpha():
            letters.add(text[i].lower())
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes