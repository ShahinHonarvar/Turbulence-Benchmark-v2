from itertools import permutations

def palindromes_between_indices(s):
    letters = sorted([char.lower() for char in s[2:7] if char.isalpha()])
    result = set()
    for permutation in permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 5:
            result.add(palindrome)
    return result or set()