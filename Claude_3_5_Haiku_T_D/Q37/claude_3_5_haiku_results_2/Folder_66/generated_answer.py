def filter_chars(text):
    result = []
    for index, char in enumerate(text):
        if 27 <= index <= 85 and 'c' <= char <= 'i':
            result.append(char)
    return ''.join((char for char in text if char not in result))