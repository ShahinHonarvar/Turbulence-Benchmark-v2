def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if not (259 <= i <= 502 and ',' <= char <= '3'):
            result.append(char)
    return ''.join(result)