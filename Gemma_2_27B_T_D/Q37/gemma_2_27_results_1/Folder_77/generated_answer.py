def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (384 <= i <= 411 and '/' <= char <= '8'):
            result.append(char)
    return ''.join(result)