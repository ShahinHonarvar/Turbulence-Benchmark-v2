import re

def palindrome_of_length_n(s):
    s = re.sub('\\W+', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 64):
        if s[i:i + 66] == s[i:i + 66][::-1]:
            palindromes.add(s[i:i + 66])
    return palindromes