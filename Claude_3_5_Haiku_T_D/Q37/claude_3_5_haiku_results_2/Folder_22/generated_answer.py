def filter_chars(s):
    chars_to_remove = set()
    for i in range(33, 71):
        if i < len(s):
            char = s[i]
            if '7' <= char <= 'k':
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))