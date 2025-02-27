def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 41 <= i <= 79 and 'f' <= char <= '|':
            continue
        result.append(char)
    return ''.join(result)