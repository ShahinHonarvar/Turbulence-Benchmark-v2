def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (42 <= i <= 92 and '/' <= char <= 'a'):
            result.append(char)
    return ''.join(result)