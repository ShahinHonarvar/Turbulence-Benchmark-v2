def filter_chars(str1):
    return ''.join([ch for ch in str1 if ch not in string.ascii_lowercase[46:68] or (ch > 'H' and ch < 's')])