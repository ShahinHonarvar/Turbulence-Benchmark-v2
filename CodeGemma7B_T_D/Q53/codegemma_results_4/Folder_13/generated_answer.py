import re

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    pattern = re.compile('([a-z])\\\\1')
    for i in range(len(text)):
        for j in range(i + 52, len(text)):
            substring = text[i:j + 1]
            if pattern.fullmatch(substring):
                palindromes.add(substring)
    return palindromes