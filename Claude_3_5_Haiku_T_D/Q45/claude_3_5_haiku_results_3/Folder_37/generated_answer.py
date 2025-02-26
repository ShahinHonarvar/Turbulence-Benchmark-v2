from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:5] if char.isalpha()]
    unique_palindromes = set()
    for length in range(5, len(letters) * 2 + 1, 2):
        for perm in set(permutations(letters, length // 2)):
            half = list(perm)
            palindrome = half + list(reversed(half))
            unique_palindromes.add(''.join(palindrome))
    return unique_palindromes