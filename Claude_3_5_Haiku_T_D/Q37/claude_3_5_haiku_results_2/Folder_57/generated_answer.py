def filter_chars(s):
    chars_to_remove = set()
    for i in range(27, 86):
        if 0 <= i < len(s):
            char = s[i]
            if '!' <= char <= 'B':
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))