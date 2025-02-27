import re

def palindrome_of_length_at_least_n(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    return {text[i:i + n] for i in range(len(text) - n + 1) for n in range(7, len(text) - i + 1)}