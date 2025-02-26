def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if 41 <= i <= 86 and 'S' <= char <= 's':
            result.extend((c for c in string if c != char))
            return ''.join(result)
    return string