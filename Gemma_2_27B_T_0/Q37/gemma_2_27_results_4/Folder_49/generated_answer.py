def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (42 <= i <= 97 and '*' <= char <= 'b'):
            result.append(char)
    return ''.join(result)