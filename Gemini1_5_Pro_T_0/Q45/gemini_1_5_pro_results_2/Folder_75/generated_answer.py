from itertools import permutations

def palindromes_between_indices(string):
    letters = set([string[i].lower() for i in range(2, 5) if string[i].isalpha()])
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes