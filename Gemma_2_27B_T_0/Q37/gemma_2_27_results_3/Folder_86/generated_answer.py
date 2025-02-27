def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (164 <= i <= 706 and 'O' <= char <= '}'):
            result.append(char)
    return ''.join(result)