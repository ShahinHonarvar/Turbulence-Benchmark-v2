from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:6] if char.isalpha()]
    palindrome_set = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for variant in [perm, perm[::-1]]:
                variant_str = ''.join(variant)
                if variant_str == variant_str[::-1] and len(variant_str) >= 6:
                    palindrome_set.add(variant_str)
    return palindrome_set