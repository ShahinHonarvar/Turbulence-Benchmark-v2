import itertools
import string

def palindromes_between_indices(s):
    s = s[1:10].lower()
    letters = [c for c in s if c in string.ascii_lowercase]
    palindromes = set()
    for p in itertools.permutations(letters, 7):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    for p in itertools.permutations(letters, 8):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    for p in itertools.permutations(letters, 9):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes