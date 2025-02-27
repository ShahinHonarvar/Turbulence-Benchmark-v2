def filter_chars(text):
    result = ''
    for index, char in enumerate(text):
        if 26 <= index <= 64 and 'V' <= char <= 'o':
            continue
        result += char
    return result