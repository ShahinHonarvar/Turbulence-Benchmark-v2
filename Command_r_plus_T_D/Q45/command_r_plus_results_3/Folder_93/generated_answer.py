import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[2:8])
    if not letters:
        return set()
    palindromes = set()
    for letter in letters:
        palindrome = letter + letter[::-1]
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes