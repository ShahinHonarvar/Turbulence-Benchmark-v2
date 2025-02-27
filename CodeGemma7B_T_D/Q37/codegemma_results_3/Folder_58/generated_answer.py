def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if 503 <= i <= 753 and c >= '9' and (c <= 'w'):
            continue
        result += c
    return result