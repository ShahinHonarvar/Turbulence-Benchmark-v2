def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if 26 <= i <= 64 and 'V' <= char <= 'o':
            result.extend((c for c in string if c != char))
            break
    else:
        result = list(string)
    return ''.join(result)