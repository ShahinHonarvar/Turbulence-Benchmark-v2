def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 384 <= i <= 411 and '/' <= char <= '8':
            continue
        result.append(char)
    return ''.join(result)