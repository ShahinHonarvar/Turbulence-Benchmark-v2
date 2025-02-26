def filter_chars(s):
    if len(s) < 10:
        return s
    chars_to_remove = set()
    for i in range(8, 10):
        if 'R' <= s[i] <= 't':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))