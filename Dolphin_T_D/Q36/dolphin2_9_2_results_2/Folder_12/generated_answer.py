def filter_chars(s):
    chars_to_remove = []
    for i in range(32, 84):
        if 'm' < chr(i) < 'w':
            chars_to_remove.append(chr(i))
    return ''.join([c for c in s if c not in chars_to_remove])