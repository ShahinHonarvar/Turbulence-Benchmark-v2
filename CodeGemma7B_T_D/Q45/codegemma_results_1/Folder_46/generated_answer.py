import itertools
import re

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text.lower())
    letters = text[4:10]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for letters in itertools.permutations(letters):
        palindrome = ''.join(letters)
        if palindrome[::-1] == palindrome:
            palindromes.add(palindrome)
    return palindromes