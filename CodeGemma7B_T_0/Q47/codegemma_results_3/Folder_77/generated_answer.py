import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = re.sub('[^a-z]', '', text)
    palindromes = set()
    for i in range(103, 277):
        for j in range(i + 100, i + 170):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes