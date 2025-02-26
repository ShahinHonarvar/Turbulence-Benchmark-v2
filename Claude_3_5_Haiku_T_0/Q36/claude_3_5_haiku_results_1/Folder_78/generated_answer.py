def filter_chars(s):
    if len(s) <= 34:
        return s
    chars_to_remove = set()
    for i in range(30, 33):
        if '%' < s[i] < 'a':
            chars_to_remove.add(s[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result