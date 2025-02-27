import re

def palindrome_of_length_at_least_n(text):
    text = re.sub('[^a-zA-Z]', '', text)
    text = text.lower()
    result = set()
    for i in range(len(text)):
        for j in range(i + 75, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                result.add(text[i:j + 1])
    return result