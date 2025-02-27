def filter_chars(text):
    result = ''
    for i, char in enumerate(text):
        if i >= 18 and i <= 31 and (char > 'H') and (char < '|'):
            continue
        result += char
    return result