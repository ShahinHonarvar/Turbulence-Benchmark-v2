import re

def palindrome_of_length_n(text):
    text = re.sub('[^a-zA-Z]', '', text)
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 80 + 1):
        for j in range(i + 80, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes