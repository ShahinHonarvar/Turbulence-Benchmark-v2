def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 722 <= i <= 832 and 'K' <= char <= 'm':
            filtered_chars.extend((c for c in s if c != char))
            return ''.join(filtered_chars)
    return s