def filter_chars(string):
    chars_to_remove = set()
    for i in range(71, 97):
        char = chr(i)
        if '_' <= char <= 'o':
            chars_to_remove.add(char)
    return ''.join((char for char in string if char not in chars_to_remove))