def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 259 <= i <= 502 and ',' <= char <= '3':
            continue
        result.append(char)
    return ''.join(result)