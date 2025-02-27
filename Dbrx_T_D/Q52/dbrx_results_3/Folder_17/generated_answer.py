import re

def palindrome_of_length_n(s):
    n = 289
    s = s.lower()
    letters = re.findall('[a-z]', s)
    if len(letters) < n:
        return set()
    palindromes = set()
    for i in range(len(letters) - n + 1):
        substring = letters[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(''.join(substring))
    return palindromes