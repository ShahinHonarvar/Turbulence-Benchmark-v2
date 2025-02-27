import re

def palindrome_of_length_n(text):
    pattern = '[a-zA-Z]{46}'
    palindromes = set()
    for i in range(len(text) - 45):
        substring = text[i:i + 46]
        if re.match(pattern, substring):
            palindromes.add(substring)
    return palindromes