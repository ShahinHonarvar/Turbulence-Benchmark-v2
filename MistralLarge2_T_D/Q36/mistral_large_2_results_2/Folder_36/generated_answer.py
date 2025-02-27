def filter_chars(s):
    chars_to_remove = set()
    for i in range(283, 484):
        if 283 < i < 484 and 'l' < s[i] < 't':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))