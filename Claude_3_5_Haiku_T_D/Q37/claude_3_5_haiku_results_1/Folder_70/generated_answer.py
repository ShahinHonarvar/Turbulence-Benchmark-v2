def filter_chars(s):
    chars_to_remove = set()
    for i in range(515, 539):
        if i < len(s):
            char = s[i]
            if '+' <= char <= '}':
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))