import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if j - i == 53 and s[i:j] == s[i:j][::-1]}