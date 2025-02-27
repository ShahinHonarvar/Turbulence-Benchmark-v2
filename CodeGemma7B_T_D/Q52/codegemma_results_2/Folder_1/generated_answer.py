import re

def palindrome_of_length_n(str):
    str = re.sub('[^a-zA-Z]', '', str)
    lowercase_str = str.lower()
    palindromes = set()
    for i in range(len(lowercase_str) - 26):
        substring = lowercase_str[i:i + 27]
        if substring == substring[::-1]:
            palindromes.add(str[i:i + 27])
    return palindromes