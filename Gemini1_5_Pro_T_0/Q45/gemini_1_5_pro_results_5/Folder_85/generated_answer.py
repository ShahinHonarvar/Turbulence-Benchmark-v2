from itertools import permutations

def palindromes_between_indices(string):
    letters = []
    for i in range(2, 9):
        if string[i].isalpha() and string[i].lower() not in letters:
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes