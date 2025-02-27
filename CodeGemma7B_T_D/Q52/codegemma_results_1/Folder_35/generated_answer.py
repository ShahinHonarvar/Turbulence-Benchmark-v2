import re

def palindrome_of_length_n(text):
    pattern = re.compile('[A-Za-z]{116}')
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 116, len(text) + 1):
            substring = text[i:j].lower()
            if pattern.fullmatch(substring):
                palindromes.add(substring)
    return palindromes