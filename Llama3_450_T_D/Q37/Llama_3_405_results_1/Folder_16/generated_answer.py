def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(225, 382) if 'D' <= chr(i) <= 'Y']
    return ''.join((c for c in s if c not in chars_to_remove))