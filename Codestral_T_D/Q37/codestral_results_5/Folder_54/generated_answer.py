def filter_chars(s):
    filtered_s = ''.join((c for i, c in enumerate(s) if i < 46 or i > 85 or c < '-' or (c > 'X')))
    return filtered_s