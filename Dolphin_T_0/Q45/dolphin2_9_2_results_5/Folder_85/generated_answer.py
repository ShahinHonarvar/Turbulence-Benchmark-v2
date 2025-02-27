from itertools import combinations, permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:9] if c.isalpha() and c.islower()]
    if len(letters) < 7:
        return set()
    palindrome_set = set()
    for c in combinations(letters, 7):
        for p in permutations(c):
            word = ''.join(p)
            if word == word[::-1]:
                palindrome_set.add(word)
    return palindrome_set