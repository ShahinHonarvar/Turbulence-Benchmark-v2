def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not 259 <= i <= 502 or not ',' <= char <= '3':
            result.append(char)
    return ''.join(result)