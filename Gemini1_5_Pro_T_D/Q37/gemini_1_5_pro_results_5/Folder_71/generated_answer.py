def filter_chars(text):
    result = ''
    for i in range(len(text)):
        char = text[i]
        if not (32 <= ord(char) <= 46 and '0' <= char <= 'k'):
            result += char
    return result