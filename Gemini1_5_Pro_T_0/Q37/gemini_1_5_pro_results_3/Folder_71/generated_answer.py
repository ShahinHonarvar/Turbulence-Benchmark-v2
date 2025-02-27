def filter_chars(text):
    result = ''
    for char in text:
        if not (32 <= ord(char) <= 46 and '0' <= char <= 'k'):
            result += char
    return result