from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:7] if c.isalpha()]
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if word == word.lower() and word == word[::-1].lower():
                palindromes.add(word)
    return palindromes