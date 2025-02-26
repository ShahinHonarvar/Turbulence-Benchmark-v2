def filter_chars(string):
    chars_to_remove = set()
    for i in range(513, 878):
        if i < len(string):
            char = string[i]
            if '?' <= char <= 'n':
                chars_to_remove.add(char)
    return ''.join((char for char in string if char not in chars_to_remove))