def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 722 <= i <= 832 and 'K' <= char <= 'm':
            continue
        result.append(char)
    return ''.join(result)