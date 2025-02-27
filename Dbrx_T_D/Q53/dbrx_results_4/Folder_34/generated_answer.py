import re

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 67):
        for j in range(i + 68):
            if j - i >= 68 and text[i:j] == text[i:j][::-1].lower():
                palindromes.add(text[i:j].lower())
    return palindromes