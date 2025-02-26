def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 31 < i < 73:
            if 'M' < char < 'j':
                filtered_chars.extend([c for c in s if c != char])
                return ''.join(filtered_chars)
    return s