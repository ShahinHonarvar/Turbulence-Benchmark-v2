def filter_chars(s):
    chars_to_remove = set()
    for i in range(33, 36):
        if chr(i) > '>' and chr(i) < 'A':
            chars_to_remove.add(chr(i))
    result = ''.join([c for c in s if c not in chars_to_remove])
    return result