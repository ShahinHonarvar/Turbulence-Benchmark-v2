def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (38 <= i <= 69 and 'H' <= char <= 'e'):
            result.append(char)
    return ''.join(result)