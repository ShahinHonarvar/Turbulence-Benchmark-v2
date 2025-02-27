def filter_chars(s):
    chars_to_filter = [char for char in s[35:60] if '!' < char < 'B']
    return ''.join((char for char in s if char not in chars_to_filter))