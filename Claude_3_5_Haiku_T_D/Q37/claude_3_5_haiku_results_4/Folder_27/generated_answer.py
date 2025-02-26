def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 43 <= i <= 80 and '=' <= char <= 'E':
            filtered_chars.extend((c for c in s if c != char))
            return ''.join(filtered_chars)
    return s