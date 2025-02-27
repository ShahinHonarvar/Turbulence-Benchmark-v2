from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:8]]
    palindromes = set()
    for p in permutations(letters, 4):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes if len(palindromes) > 0 else set()