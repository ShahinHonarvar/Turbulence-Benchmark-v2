from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join((ch.lower() for ch in s[3:9] if ch.isalpha()))
    if len(substring) < 5:
        return set()
    palindromes = set()
    for length in range(5, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes