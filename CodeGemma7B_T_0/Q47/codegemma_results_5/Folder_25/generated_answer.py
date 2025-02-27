import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = re.sub('[^a-z]', '', text)
    text = text[26:85]
    palindromes = set()
    for i in range(len(text) - 2):
        for j in range(i + 2, len(text)):
            if text[i] == text[j]:
                palindrome = text[i:j + 1]
                if 30 <= len(palindrome) <= 46:
                    palindromes.add(palindrome)
    return palindromes