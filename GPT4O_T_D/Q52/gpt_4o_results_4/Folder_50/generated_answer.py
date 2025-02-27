import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    for i in range(len(s) - 39):
        substring = s[i:i + 40]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes