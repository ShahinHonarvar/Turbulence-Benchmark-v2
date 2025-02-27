def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (35 <= i <= 98 and 'A' <= char <= 'b'):
            result.append(char)
    return ''.join(result)