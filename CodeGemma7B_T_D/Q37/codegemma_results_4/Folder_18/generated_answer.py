def filter_chars(str):
    return ''.join([c for c in str if not (770 <= ord(c) <= 970 and ord(c) >= '-')])