from itertools import permutations
import string

def palindromes_between_indices(txt):
    letters = ''.join([letter for letter in txt.lower() if letter in string.ascii_lowercase and txt.index(letter) <= 5])
    if len(letters) < 6:
        return set()
    palindromes = set()
    for permutation in permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes