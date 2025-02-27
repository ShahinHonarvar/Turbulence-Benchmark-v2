from itertools import permutations

def palindromes_between_indices(string):
    letters = set()
    for i in range(4, 10):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.add(string[i].lower())
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes