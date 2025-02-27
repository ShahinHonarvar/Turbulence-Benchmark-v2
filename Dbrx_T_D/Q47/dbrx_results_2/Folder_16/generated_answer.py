import re

def palindromes_of_specific_lengths(s):
    s = s[15:87]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 51, i + 61) if s[i:j] == s[i:j][::-1]}
    return palindromes