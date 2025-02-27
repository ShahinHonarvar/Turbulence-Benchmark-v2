import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = re.sub('[^a-z]', '', text)
    text = text[70:141]
    return {word for word in text.split() if len(word) in range(3, 61) and word == word[::-1]}