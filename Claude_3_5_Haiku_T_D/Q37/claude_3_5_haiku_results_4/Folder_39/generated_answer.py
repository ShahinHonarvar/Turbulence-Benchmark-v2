def filter_chars(text):
    result = ''
    for i, char in enumerate(text):
        if 52 <= i <= 81 and 'A' <= char <= 'U':
            result += ''.join((c for c in text if c != char))
            return result
    return text