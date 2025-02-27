def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (38 <= i <= 69 and 'H' <= char <= 'e'):
            result.append(char)
    return ''.join(result)