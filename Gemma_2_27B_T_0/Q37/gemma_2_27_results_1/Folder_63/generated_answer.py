def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (42 <= i <= 92 and '/' <= char <= 'a'):
            result.append(char)
    return ''.join(result)