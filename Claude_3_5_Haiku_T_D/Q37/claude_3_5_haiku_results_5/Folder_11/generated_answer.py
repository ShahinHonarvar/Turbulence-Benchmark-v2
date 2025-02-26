def filter_chars(s):
    chars_to_remove = set()
    for i in range(29, 98):
        if 29 <= i <= 97:
            char = s[i]
            if '-' <= char <= 'n':
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))