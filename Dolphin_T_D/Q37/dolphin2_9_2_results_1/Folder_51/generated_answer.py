def filter_chars(text):
    result = ''
    for i, char in enumerate(text):
        if i < 36 or i > 40:
            result += char
        elif 'H' <= char <= 'e':
            continue
        else:
            result += char
    return result