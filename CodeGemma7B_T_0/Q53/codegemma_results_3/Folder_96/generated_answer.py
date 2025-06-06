import re

def palindrome_of_length_at_least_n(text):
    text = re.sub('[^a-zA-Z]', '', text)
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 24, len(text) + 1):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes