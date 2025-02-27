import re

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    text = text[2:8]
    if len(text) < 3:
        return set()
    return {text[i:i + 3] for i in range(len(text) - 2)}