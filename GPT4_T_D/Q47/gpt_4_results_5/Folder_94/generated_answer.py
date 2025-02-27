import re

def palindromes_of_specific_lengths(text):
    text = text[40:95]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 45, min(i + 52, len(text) + 1)):
            substr = text[i:j]
            letters_only = re.sub('[^a-zA-Z]', '', substr)
            if letters_only.lower() == letters_only[::-1].lower():
                palindromes.add(substr)
    return palindromes