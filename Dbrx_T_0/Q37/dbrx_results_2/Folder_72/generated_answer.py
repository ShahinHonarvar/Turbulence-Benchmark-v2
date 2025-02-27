def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (35 <= i <= 51 and 'H' <= c <= 's')]
    return ''.join(filtered_chars)