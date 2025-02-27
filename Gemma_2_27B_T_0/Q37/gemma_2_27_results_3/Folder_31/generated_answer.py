def filter_chars(s):
    result = []
    for char in s:
        if 57 <= ord(char) <= 96 and '<' <= char <= 'w':
            continue
        result.append(char)
    return ''.join(result)