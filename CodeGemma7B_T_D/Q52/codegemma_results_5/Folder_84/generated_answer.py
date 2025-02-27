import re

def palindrome_of_length_n(text):
    if not isinstance(text, str):
        raise TypeError('Input must be a string')
    text = re.sub('[^a-zA-Z]', '', text)
    text = text.lower()
    palindromes = set()
    n = 131
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes