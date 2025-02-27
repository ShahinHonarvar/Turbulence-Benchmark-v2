import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = re.sub('[^a-z]', '', text)
    text = text[124:284]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 115, i + 135):
            if j <= len(text):
                if text[i:j] == text[j - 1:i - 1:-1]:
                    palindromes.add(text[i:j])
    return palindromes