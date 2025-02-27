def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (40 <= i <= 63 and 'K' <= c <= ']')]
    return ''.join(filtered_classes)