from itertools import combinations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    palindromes = set()
    for r in range(3, len(s) + 1):
        for combo in combinations(s, r):
            word = ''.join(combo)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes