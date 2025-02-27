from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(sorted(s[1:4]))
    length = len(substring)
    palindromes = set()
    for p in permutations(substring, length):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes if len(palindromes) > 0 else set()