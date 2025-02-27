import re

def palindrome_of_length_n(s):
    s = re.findall('[a-zA-Z]', s)
    n = 40
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(''.join(substring))
    return palindromes