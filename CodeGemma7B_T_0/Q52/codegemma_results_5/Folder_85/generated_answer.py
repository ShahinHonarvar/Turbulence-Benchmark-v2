import re

def palindrome_of_length_n(text):
    text = text.lower()
    text = re.sub('[^a-z]', '', text)
    palindromes = set()
    for i in range(len(text) - 45):
        for j in range(i + 46, len(text) + 1):
            if text[i:j] == text[j - 1:i - 1:-1]:
                palindromes.add(text[i:j])
    return palindromes