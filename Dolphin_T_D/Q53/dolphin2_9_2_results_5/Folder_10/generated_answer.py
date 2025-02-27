import re

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    res = re.findall('[a-zA-Z]{92,}', text)
    if not res:
        return palindromes
    for word in res:
        if word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes