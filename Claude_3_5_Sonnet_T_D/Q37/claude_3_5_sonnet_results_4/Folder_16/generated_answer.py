def filter_chars(string):
    chars_to_remove = set()
    for i in range(225, 382):
        if i < len(string) and 'D' <= string[i] <= 'Y':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))