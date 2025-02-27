import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = re.sub('[^a-z]', '', text)
    palindromes = set()
    for i in range(33, 86):
        for j in range(i - 25, i + 1):
            if j >= 0 and j + 25 - i < len(text) and (text[i - j - 1:i + j + 1] == text[i - j - 1:i + j + 1][::-1]):
                palindromes.add(text[i - j - 1:i + j + 1])
    return palindromes