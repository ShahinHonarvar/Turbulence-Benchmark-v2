from itertools import permutations

def palindromes_between_indices(string):
    letters = set()
    for i in range(1, 8):
        if string[i].isalpha():
            letters.add(string[i].lower())
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for j in permutations(letters, i):
            word = ''.join(j)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes