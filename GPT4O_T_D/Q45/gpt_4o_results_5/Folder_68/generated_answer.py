from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join((ch.lower() for ch in s[1:9] if ch.isalpha()))
    palindromes = set()
    for p in permutations(substring):
        word = ''.join(p)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes