def filter_chars(s):
    filtered = ''
    for i, char in enumerate(s):
        if 51 <= i <= 96 and 'X' <= char <= 'p':
            filtered += ''.join((c for c in s if c != char))
            return filtered
    return s