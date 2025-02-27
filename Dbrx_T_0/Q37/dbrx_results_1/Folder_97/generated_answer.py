def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (227 <= i <= 235 and 'D' <= c <= 'u')]
    return ''.join(filtered_chars)