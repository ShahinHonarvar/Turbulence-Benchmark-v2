def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (41 <= i <= 86 and 'S' <= c <= 's')]
    return ''.join(filtered_chars)