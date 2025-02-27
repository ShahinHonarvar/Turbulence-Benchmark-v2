import re

def palindrome_of_length_n(text):
    return {text[i:i + 289] for i in range(len(text)) if re.match('^[a-zA-Z]{289}$', text[i:i + 289])}