def filter_chars(s):
    chars_to_remove = set()
    for i in range(476, 948):
        if 'b' < s[i] < 'd':
            chars_to_remove.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])