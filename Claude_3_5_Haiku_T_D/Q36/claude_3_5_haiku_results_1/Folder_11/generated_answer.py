def filter_chars(string):
    if len(string) <= 94:
        return string
    chars_to_remove = set()
    for i in range(87, 93):
        if 'E' < string[i] < '~':
            chars_to_remove.add(string[i])
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result