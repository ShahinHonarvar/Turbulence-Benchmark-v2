import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    substring = text[31:92]
    palindromes = set()
    for i in range(len(substring) - 49):
        for j in range(i + 50, len(substring) - 3):
            if substring[i:j + 1] == substring[j:i:-1]:
                palindromes.add(substring[i:j + 1])
    return palindromes