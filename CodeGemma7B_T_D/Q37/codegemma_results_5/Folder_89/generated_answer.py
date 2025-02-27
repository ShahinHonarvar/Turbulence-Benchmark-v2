def filter_chars(text):
    result = ''
    start, end = (11, 32)
    for char in text:
        if start <= text.index(char) <= end and char >= '!' and (char <= '@'):
            continue
        result += char
    return result