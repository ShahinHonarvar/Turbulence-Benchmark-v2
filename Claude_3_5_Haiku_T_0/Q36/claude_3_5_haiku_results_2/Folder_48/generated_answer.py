def filter_chars(s):
    chars_to_remove = set()
    for i in range(155, 222):
        if 'A' < s[i] < 'f':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))