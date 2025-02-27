def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(33, 61) if '3' < chr(i) < 'D']
    return ''.join([c for c in s if c not in chars_to_remove])