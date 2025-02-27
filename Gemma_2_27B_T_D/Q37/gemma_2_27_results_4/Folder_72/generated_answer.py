def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if not (35 <= i <= 51 and 'H' <= char <= 's'):
            result.append(char)
    return ''.join(result)