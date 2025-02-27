def filter_chars(string):
    filtered_chars = [c for c in string if not (24 <= string.index(c) <= 82 and '5' <= c <= '<')]
    return ''.join(filtered_chars)