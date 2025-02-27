from itertools import permutations

def palindromes_between_indices(string):
    substring = string[3:6].lower()
    palindromes = set()
    for i in range(3, len(substring) + 1):
        for p in permutations(substring, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes