def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (722 <= i <= 832 and 'K' <= c <= 'm')]
    return ''.join(filtered_chars)