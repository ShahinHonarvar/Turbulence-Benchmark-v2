import re

def palindrome_of_length_n(s):
    s = s.lower()
    letters = re.findall('[a-z]', s)
    if len(s) < 41:
        return set()
    palindromes = set()
    for i in range(len(letters) - 40):
        substring = ''.join(letters[i:i + 41])
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes