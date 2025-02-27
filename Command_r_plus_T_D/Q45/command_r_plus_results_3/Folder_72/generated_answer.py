import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[1:8])
    letters = ''.join(letters).lower()
    palindromes = set()
    for i in range(len(letters) - 5):
        for j in range(i + 1, len(letters) - (i + 1)):
            palindrome = letters[i:j] + letters[i:j][::-1]
            palindromes.add(palindrome)
    return palindromes