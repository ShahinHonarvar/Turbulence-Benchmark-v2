def filter_chars(s):
    filtered_chars = ''
    for i, char in enumerate(s):
        if 19 <= i <= 90 and 'F' <= char <= 'h':
            filtered_chars += ''.join((c for c in s if c != char))
        else:
            filtered_chars = s
    return filtered_chars