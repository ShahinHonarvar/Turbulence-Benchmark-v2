from itertools import permutations

def palindromes_between_indices(s):
    substring = s[7:9].lower()
    palindromes = set()
    for p in permutations(substring, len(substring)):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes