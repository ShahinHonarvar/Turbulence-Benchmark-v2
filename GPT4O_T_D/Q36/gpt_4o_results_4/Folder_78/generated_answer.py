def filter_chars(s):
    if len(s) < 33:
        return s
    chars_to_remove = set()
    for i in range(30, 33):
        if '%' < s[i] < 'a':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result