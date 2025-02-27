from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(set(s[3:10])))
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes