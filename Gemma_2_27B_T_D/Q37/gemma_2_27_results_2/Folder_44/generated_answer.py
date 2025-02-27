def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (21 <= i <= 43 and '+' <= char <= '8'):
            result.append(char)
    return ''.join(result)