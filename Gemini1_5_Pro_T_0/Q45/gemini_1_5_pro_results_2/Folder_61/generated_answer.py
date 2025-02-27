from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(8):
        if string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if len(word) >= 7 and word == word[::-1]:
                palindromes.add(word)
    return palindromes