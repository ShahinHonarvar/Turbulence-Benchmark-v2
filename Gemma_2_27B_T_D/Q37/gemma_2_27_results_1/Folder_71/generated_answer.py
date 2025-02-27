def filter_chars(text):
    result = []
    for char in text:
        if 32 <= ord(char) <= 46 and '0' <= char <= 'k':
            continue
        result.append(char)
    return ''.join(result)