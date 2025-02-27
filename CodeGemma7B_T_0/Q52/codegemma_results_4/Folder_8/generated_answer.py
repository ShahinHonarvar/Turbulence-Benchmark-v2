import re

def palindrome_of_length_n(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    return {text[i:i + 49] for i in range(len(text) - 49 + 1)}