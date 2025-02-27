def filter_chars(s):
    chars_to_filter = [chr(i) for i in range(32, 61) if '3' < chr(i) < 'D']
    return ''.join([c for c in s if c not in chars_to_filter])