def filter_chars(s):
    if len(s) < 75:
        return s
    chars_to_remove = set()
    for i in range(73, 75):
        if 'U' <= s[i] <= 'l':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))