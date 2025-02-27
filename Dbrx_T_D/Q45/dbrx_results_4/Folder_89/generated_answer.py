import itertools
import string

def palindromes_between_indices(s):
    s = s.lower()
    letters = s[5:10]
    english_letters = [letter for letter in letters if letter in string.ascii_lowercase]
    if len(english_letters) < 6:
        return set()
    else:
        palindromes = {''.join(letter_set) for letter_set in itertools.combinations_with_replacement(english_letters, 6)}
        return {palindrome for palindrome in palindromes if palindrome == palindrome[::-1]}