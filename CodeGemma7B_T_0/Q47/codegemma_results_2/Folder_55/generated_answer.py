import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = re.sub('[^a-z]', '', text)
    text = text[10:76]
    palindromes = set()
    for i in range(len(text) - 9):
        for j in range(i + 10, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                palindromes.add(text[i:j + 1])
    return palindromes