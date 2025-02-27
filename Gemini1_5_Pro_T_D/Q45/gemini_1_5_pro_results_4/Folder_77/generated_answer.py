from itertools import permutations

def palindromes_between_indices(string):
    letters = set([string[i].lower() for i in range(4, 7) if string[i].isalpha()])
    palindromes = set()
    for i in range(4, len(string) + 1, 2):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)
    return palindromes