def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(51, 97) if 'X' <= chr(i) <= 'p']
    return ''.join((c for c in s if c not in chars_to_remove))