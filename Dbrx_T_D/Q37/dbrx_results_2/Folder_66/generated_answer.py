def filter_chars(s):
    filtered_chars = [char for i, char in enumerate(s) if not (27 <= i <= 85 and 'c' <= char <= 'i')]
    return ''.join(filtered_chars)