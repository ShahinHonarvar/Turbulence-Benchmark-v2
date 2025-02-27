def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (54 <= i <= 83 and 'j' <= c <= 'v')]
    return ''.join(filtered_chars)