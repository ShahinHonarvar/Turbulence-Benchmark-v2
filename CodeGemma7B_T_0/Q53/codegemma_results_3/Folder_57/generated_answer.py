import re

def palindrome_of_length_at_least_n(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes