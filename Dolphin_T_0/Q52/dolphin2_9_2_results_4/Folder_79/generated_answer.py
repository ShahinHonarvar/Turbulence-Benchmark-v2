import re

def palindrome_of_length_n(s):
    s = re.sub('\\W+', '', s).lower()
    palindromes = set()
    for i in range(len(s) - 62):
        if s[i:i + 32] == s[i:i + 32][::-1]:
            palindromes.add(s[i:i + 64])
    return palindromes