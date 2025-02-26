def filter_chars(string):
    chars_to_remove = set()
    for i in range(331, 713):
        if 'M' < string[i] < '_':
            chars_to_remove.add(string[i])
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result