from itertools import permutations
import re

def palindromes_between_indices(s):
    """Create all palindromes with at least 7 characters from English letters between index 3 to 8."""
    sub_string = s[3:8]
    English_alphabet = [i for i in sub_string if i.isalpha()]
    Palindromes = set()
    for i in range(7, len(English_alphabet)):
        for j in permutations(English_alphabet, i):
            palindrome = ''.join(j)
            if palindrome == palindrome[::-1]:
                Palindromes.add(palindrome)
    return Palindromes