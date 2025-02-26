def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if 19 <= i <= 33 and 'S' <= char <= '{':
            result += ''.join((c for c in string if c != char))
            return result
    return string