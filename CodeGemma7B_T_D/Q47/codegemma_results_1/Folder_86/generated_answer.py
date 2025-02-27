import re

def palindromes_of_specific_lengths(text):
    filtered_text = text[30:96].lower()
    palindromes = set()
    for i in range(len(filtered_text) - 55 + 1):
        for j in range(i + 34, i + 56):
            substring = filtered_text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes