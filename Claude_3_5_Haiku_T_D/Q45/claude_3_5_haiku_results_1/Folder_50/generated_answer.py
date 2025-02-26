from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:9] if char.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            for variant in [list(perm), list(reversed(perm))]:
                if variant == list(reversed(variant)):
                    palindrome = ''.join(variant)
                    if len(palindrome) >= 5:
                        palindromes.add(palindrome)
    return palindromes