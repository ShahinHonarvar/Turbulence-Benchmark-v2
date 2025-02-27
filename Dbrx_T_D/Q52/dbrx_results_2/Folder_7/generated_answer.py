import re

def palindrome_of_length_n(s):
    n = 416
    letters_only = re.sub('[^a-zA-Z]', '', s).lower()
    if n > len(letters_only):
        return set()
    palindromes = set()
    for i in range(len(letters_only) - n + 1):
        substring = letters_only[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes