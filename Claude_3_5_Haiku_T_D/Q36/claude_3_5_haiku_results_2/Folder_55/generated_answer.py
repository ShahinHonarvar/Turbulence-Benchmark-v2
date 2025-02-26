def filter_chars(string):
    if len(string) <= 4:
        return string
    chars_to_remove = set()
    for i in range(4, len(string) - 1):
        if 'Y' < string[i] < 's':
            chars_to_remove.add(string[i])
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result