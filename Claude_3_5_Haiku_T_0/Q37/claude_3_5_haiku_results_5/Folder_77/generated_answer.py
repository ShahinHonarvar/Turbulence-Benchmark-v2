def filter_chars(s):
    chars_to_remove = set()
    for i in range(384, 412):
        if i < len(s):
            char = s[i]
            if '/' <= char <= '8':
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))