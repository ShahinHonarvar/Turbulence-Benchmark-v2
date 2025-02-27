import re

def palindromes_of_specific_lengths(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    palindromes = set()
    for i in range(23, 95):
        for j in range(i + 17, min(i + 56, 95)):
            word = text[i:j + 1]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes