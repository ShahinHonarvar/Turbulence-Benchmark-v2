from itertools import permutations

def palindromes_between_indices(S):
    letters = ''.join([c for c in S[3:10] if c.isalpha()])
    palindromes = set()
    for p in permutations(letters, 5):
        word = ''.join(p).lower()
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes