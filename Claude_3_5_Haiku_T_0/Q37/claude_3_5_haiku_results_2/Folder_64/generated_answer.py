def filter_chars(s):
    chars_to_remove = set()
    for i in range(1, 8):
        if 'L' <= s[i] <= 'a':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))