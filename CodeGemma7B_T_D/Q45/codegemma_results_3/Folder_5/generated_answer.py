from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    for permutation in permutations(s[4:9]):
        palindrome = ''.join((p for p in permutation if p.isalpha()))
        if len(palindrome) >= 4:
            result.add(palindrome.lower())
    return result