import re

def palindrome_of_length_n(s):
    s = re.findall('[a-zA-Z]', s)
    s = [x.lower() for x in s]
    if len(s) < 84:
        return set()
    palindromes = set()
    for i in range(len(s) - 83):
        if s[i:i + 84] == s[i:i + 84][::-1]:
            palindromes.add(''.join(s[i:i + 84]))
    return palindromes