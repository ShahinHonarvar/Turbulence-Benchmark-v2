from itertools import permutations

def palindromes_between_indices(s):
    letters_between_indices = ''.join(sorted([c for c in s[2:10] if c.isalpha()]))
    palindromes = set()
    for i in range(len(letters_between_indices)):
        for p in permutations(letters_between_indices, i + 1):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 7:
                palindromes.add(word.lower())
    return palindromes