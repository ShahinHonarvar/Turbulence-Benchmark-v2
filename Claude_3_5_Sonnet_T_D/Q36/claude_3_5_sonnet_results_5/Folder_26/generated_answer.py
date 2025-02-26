def filter_chars(string):
    chars_to_remove = set()
    for i in range(44, 83):
        if i < len(string) and ':' < string[i] < 'Q':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))