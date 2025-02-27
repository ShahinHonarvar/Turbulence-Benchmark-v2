import re

def palindrome_of_length_at_least_n(text):
    text = re.sub('[^A-Za-z]', '', text)
    text = text.lower()
    result = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            palindrome = text[i:j + 1]
            if palindrome == palindrome[::-1] and len(palindrome) >= 112:
                result.add(palindrome)
    return result