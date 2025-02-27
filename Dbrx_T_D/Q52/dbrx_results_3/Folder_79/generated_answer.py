import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i, min(len(s), i + 65)) if s[i:j] == s[i:j][::-1]}
    return palindromes