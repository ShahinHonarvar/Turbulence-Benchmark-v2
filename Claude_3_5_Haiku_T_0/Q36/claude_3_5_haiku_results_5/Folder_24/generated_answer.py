def filter_chars(s):
    if len(s) <= 11:
        return s
    chars_to_remove = set()
    for i in range(11, 15):
        if 't' < s[i] < 'v':
            chars_to_remove.add(s[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result