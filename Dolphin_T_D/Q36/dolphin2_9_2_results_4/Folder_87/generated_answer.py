def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(32, 61) if chr(i) > '3' and chr(i) < 'D']
    return ''.join([c for c in s if c not in chars_to_remove])