def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 10 <= i <= 69 and 'I' <= char <= 'K':
            continue
        result.append(char)
    return ''.join(result)