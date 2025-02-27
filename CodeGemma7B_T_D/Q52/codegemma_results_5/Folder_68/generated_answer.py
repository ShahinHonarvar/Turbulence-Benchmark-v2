import re

def palindrome_of_length_n(text):
    text = re.sub('[^a-zA-Z]', '', text)
    text = text.lower()
    n = 76
    palindromes = set()
    for i in range(len(text) - n + 1):
        for j in range(i + n):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes