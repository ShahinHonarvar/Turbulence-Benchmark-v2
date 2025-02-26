def filter_chars(string):
    if len(string) <= 6:
        return string
    chars_to_remove = set()
    for i in range(4, 5):
        if 'Y' < string[i] < 's':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))