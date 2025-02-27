def filter_chars(str):
    result = ''
    for i, char in enumerate(str):
        if i < 24 or i >= 37 or (char > 'A' and char < 'h'):
            result += char
    return result