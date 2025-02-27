from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:10] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 5 and word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes