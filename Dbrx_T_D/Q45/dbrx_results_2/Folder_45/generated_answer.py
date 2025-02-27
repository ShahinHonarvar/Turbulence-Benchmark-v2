from collections import defaultdict
import string

def palindromes_between_indices(s):
    english_letters = set(string.ascii_letters) - set(string.punctuation) - set(string.digits)
    s = s.lower()
    s = ''.join((c for c in s if c in english_letters))
    if len(s) <= 4 or len(s) < len(set(range(5, 10)) & set(range(len(s)))):
        return set()
    palindromes = set()
    for i in range(5, 10):
        for j in range(i, 10):
            current_palindrome = s[i:j + 1]
            if current_palindrome == current_palindrome[::-1]:
                palindromes.add(current_palindrome)
    return palindromes