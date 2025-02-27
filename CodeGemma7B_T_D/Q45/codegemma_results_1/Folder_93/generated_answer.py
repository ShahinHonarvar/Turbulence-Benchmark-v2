from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(text):
    text_low = text.lower()
    letters = [c for c in text_low if c in ascii_lowercase and text_low.index(c) in range(2, 7)]
    permutations_list = list(permutations(letters))
    result = []
    for permutation in permutations_list:
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1] and len(palindrome) >= 6:
            result.append(palindrome)
    return set(result)