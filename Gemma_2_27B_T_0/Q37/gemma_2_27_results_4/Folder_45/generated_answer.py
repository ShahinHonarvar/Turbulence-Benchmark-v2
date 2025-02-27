def filter_chars(s):
    result = []
    for char in s:
        if 72 <= ord(char) <= 94 and '.' <= char <= 'b':
            continue
        result.append(char)
    return ''.join(result)