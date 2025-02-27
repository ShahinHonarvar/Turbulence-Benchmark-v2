def filter_chars(text):
    result = []
    for char in text:
        if 33 <= ord(char) <= 70 and ord('7') <= ord(char) <= ord('k'):
            continue
        result.append(char)
    return ''.join(result)