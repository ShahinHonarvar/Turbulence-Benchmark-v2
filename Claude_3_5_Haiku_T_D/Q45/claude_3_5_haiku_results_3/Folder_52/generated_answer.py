from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters_in_range = [c for c in s[:8] if c.isalpha()]
    unique_palindromes = set()
    for length in range(6, len(letters_in_range) + 1):
        for perm in permutations(letters_in_range, length):
            for i in range(len(perm) + 1):
                palindrome = list(perm[:i] + tuple(reversed(perm[i:])))
                if palindrome == list(reversed(palindrome)) and len(palindrome) >= 6:
                    unique_palindromes.add(''.join(palindrome))
    return unique_palindromes