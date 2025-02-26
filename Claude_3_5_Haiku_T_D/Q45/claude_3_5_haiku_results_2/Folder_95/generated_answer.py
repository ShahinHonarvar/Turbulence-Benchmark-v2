from itertools import permutations

def palindromes_between_indices(string):
    chars_in_range = string[7:9]
    english_letters = [char.lower() for char in chars_in_range if char.isalpha()]
    if len(english_letters) < 3:
        return set()
    palindrome_set = set()
    for length in range(3, len(english_letters) + 1):
        for perm in set(permutations(english_letters, length)):
            for variant in (perm, perm[::-1]):
                if variant == variant[::-1]:
                    palindrome = ''.join(variant)
                    palindrome_set.add(palindrome)
    return palindrome_set