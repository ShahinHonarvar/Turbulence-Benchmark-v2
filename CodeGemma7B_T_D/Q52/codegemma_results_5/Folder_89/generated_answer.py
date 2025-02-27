from re import finditer

def palindrome_of_length_n(word):
    pattern = '[a-zA-Z]{37}'
    return {word[m.start():m.end()] for m in finditer(pattern, word, flags=re.IGNORECASE)}