def filter_chars(s):
    result = []
    for char in s:
        if 33 <= ord(char) <= 70 and '7' <= char <= 'k':
            continue
        result.append(char)
    return ''.join(result)