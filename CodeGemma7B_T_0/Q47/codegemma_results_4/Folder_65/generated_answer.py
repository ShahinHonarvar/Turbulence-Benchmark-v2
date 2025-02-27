import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = re.sub('[^a-z]', '', text)
    text = text[15:95 + 1]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 20, min(i + 66 + 1, len(text))):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes