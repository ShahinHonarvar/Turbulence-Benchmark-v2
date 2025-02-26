from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:6] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) * 2 + 1, 2):
        for perm in set(permutations(letters, length // 2)):
            half = list(perm)
            full_palindrome = half + list(reversed(half))
            palindrome_str = ''.join(full_palindrome)
            if len(palindrome_str) >= 4:
                palindromes.add(palindrome_str)
    return palindromes