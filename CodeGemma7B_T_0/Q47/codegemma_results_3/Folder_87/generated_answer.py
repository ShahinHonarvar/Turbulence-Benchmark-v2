import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = re.sub('[^a-z]', '', text)
    text = text[11:94]
    palindromes = set()
    for i in range(len(text) - 33):
        for j in range(i + 34, len(text) + 1):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes