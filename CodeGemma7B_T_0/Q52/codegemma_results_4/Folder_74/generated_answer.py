import re

def palindrome_of_length_n(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    palindromes = set()
    for i in range(len(text) - 95):
        for j in range(i + 96, len(text) + 1):
            if text[i:j] == text[j - 96:i:-1]:
                palindromes.add(text[i:j])
    return palindromes