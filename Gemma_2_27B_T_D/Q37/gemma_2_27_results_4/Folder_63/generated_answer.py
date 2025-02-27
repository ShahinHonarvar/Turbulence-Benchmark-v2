def filter_chars(s):
    chars_to_remove = set()
    for i in range(42, 93):
        if chr(i) >= '/' and chr(i) <= 'a':
            chars_to_remove.add(chr(i))
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result