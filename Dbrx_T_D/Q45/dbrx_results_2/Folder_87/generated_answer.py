import re
    import string

def palindromes_between_indices(string):
    english_letters = set(string.ascii_letters)
    substring = re.findall('[a-zA-Z]{3,}', string[3:10])
    palindromes = set()
    for word in substring:
        if set(word.lower()).issubset(english_letters) and word == word[::-1]:
            palindromes.add(word.lower())
    return palindromes