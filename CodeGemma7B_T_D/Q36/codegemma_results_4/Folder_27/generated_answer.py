import string

def filter_chars(text):
    filtered = ''
    for i, char in enumerate(text):
        if i >= 48 and i < 75 and (char > '6') and (char < '_'):
            continue
        filtered += char
    return filtered