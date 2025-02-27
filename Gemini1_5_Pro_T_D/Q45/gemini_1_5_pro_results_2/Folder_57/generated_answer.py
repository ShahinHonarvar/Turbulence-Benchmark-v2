from itertools import permutations

def palindromes_between_indices(string):
    letters = set()
    for i in range(2, 6):
        if string[i].isalpha():
            letters.add(string[i].lower())
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for p in permutations(letters, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes