import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(30):
        for j in range(i + 20, min(i + 31, len(text))):
            if text[i] == text[j] and text[i + 1:j].isalpha():
                palindromes.add(text[i:j + 1])
    return palindromes