def filter_chars(s):
    if len(s) < 10:
        return s
    chars_to_remove = set()
    for i in range(7, 10):
        if '6' <= s[i] <= 'w':
            chars_to_remove.add(s[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result