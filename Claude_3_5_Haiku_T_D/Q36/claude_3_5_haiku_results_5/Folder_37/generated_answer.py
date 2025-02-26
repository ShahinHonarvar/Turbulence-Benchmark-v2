def filter_chars(string):
    chars_to_remove = set()
    for i in range(45, 59):
        if '/' < string[i] < '6':
            chars_to_remove.add(string[i])
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result