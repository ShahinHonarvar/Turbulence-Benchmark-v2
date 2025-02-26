def filter_chars(s):
    chars_to_remove = set()
    for i in range(61, 71):
        if 0 <= i < len(s):
            char = s[i]
            if '0' <= char <= '@':
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))