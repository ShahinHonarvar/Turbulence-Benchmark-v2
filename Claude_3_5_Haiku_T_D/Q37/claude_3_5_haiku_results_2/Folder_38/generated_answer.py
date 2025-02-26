def filter_chars(text):
    result = ''
    for i, char in enumerate(text):
        if 24 <= i <= 79 and 'a' <= char <= 'f':
            result += ''.join((c for c in text if c != char))
            break
        result += char
    return result if len(result) > 0 else text