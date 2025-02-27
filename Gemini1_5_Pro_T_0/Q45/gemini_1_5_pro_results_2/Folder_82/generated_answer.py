from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(1, 7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for j in permutations(letters, i):
            word = ''.join(j)
            if word == word[::-1] and len(word) >= 7:
                palindromes.add(word)
    return palindromes