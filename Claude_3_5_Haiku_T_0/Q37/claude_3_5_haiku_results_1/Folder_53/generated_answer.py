def filter_chars(s):
    chars_to_remove = set()
    for i in range(83, 100):
        if i < len(s):
            char = s[i]
            if '*' <= char <= 'j':
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))