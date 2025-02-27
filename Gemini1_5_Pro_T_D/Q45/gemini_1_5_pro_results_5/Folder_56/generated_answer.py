from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = Counter([c.lower() for c in s[5:10] if c.isalpha()])
    palindromes = set()
    for n in range(5, len(letters) + 1):
        for p in permutations(letters.elements(), n):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 5:
                palindromes.add(word)
    return palindromes