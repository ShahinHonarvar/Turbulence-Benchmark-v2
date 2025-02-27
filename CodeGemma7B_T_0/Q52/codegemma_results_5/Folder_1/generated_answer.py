import re

def palindrome_of_length_n(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    return {text[i:i + 27] for i in range(len(text) - 26)}