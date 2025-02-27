from itertools import permutations, combinations_with_replacement
import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[:9])
    letters = [letter.lower() for letter in letters]
    letters_set = set(letters)
    palindromes = set()
    for first_half_len in range(3, 4):
        for center in letters_set:
            for first_half in combinations_with_replacement(letters_set, first_half_len):
                palindrome = ''.join(first_half) + center + ''.join(reversed(first_half))
                palindromes.add(palindrome)
    return palindromes