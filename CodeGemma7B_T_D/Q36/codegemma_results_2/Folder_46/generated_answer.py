def filter_chars(string):
    return ''.join([ch for ch in string if not (ch > '<' and ch < 'C' and (19 < string.index(ch) < 69))])