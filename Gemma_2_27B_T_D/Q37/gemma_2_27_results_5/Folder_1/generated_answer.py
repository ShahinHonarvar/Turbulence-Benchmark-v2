def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (41 <= i <= 79 and 'f' <= char <= '|'):
            result.append(char)
    return ''.join(result)