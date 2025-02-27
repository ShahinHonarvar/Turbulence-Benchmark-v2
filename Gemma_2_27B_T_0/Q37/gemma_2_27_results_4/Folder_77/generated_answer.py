def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (384 <= i <= 411 and '/' <= char <= '8'):
            result.append(char)
    return ''.join(result)