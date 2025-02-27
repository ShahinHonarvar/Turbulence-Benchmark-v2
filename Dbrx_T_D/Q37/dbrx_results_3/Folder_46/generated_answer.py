def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not 11 <= i <= 72 or not 'i' <= c <= 'v']
    return ''.join(filtered_chars)