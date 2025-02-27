import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 474):
        if re.match('^[a-zA-Z]*$', s[i:i + 475]) and s[i:i + 475] == s[i:i + 475][::-1]:
            palindromes.add(s[i:i + 475])
    return palindromes