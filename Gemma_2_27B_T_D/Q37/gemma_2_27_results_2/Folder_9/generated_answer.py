def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if not (38 <= i <= 99 and 'A' <= char <= 'Q'):
            result.append(char)
    return ''.join(result)