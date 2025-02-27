def filter_chars(s):
    char_range = [ch for ch in s if 331 <= s.index(ch) < 713 and 'M' < ch < '_']
    return ''.join([ch for ch in s if ch not in char_range])