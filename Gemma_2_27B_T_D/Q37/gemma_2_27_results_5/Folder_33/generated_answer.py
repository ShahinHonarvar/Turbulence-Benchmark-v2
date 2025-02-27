def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 722 <= i <= 832 and 'K' <= char <= 'm':
            continue
        result.append(char)
    return ''.join(result)