import re

def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    letters_only = re.findall('[a-z]', s)
    if len(letters_only) < 97:
        return palindromes
    for i in range(len(letters_only) - 97 + 1):
        substring = ''.join(letters_only[i:i + 97])
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes