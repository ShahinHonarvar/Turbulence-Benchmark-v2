def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (58 < i < 81 and '5' < c < '>')]
    return ''.join(filtered_chars)