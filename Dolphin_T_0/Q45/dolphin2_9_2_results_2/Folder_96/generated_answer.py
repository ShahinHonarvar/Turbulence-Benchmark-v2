from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:9]
    palindromes = set()
    for p in permutations(substring):
        word = ''.join(p)
        if len(word) >= 6 and word == word[::-1]:
            palindromes.add(word.lower())
    return palindromes