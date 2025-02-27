import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = re.sub('[^a-z]', '', text)
    palindromes = set()
    for i in range(100, 296):
        for j in range(i + 136, i + 161):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes