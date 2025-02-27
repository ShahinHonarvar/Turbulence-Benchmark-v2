import re

def palindromes_of_specific_lengths(text):
    text = text[10:76].lower()
    palindromes = set()
    for i in range(len(text) - 9):
        for j in range(10, 21):
            if i + j <= len(text) and text[i:i + j] == text[i:i + j][::-1] and (len(re.findall('[a-z]', text[i:i + j])) == j):
                palindromes.add(text[i:i + j])
    return palindromes