import re

def palindrome_of_length_n(s):
    s = s.lower()
    letters = re.findall('[a-z]', s)
    if len(letters) < 78:
        return set()
    palindromes = set()
    for i in range(len(letters) - 78 + 1):
        substring = letters[i:i + 78]
        if substring == substring[::-1]:
            palindromes.add(''.join(substring))
    return palindromes