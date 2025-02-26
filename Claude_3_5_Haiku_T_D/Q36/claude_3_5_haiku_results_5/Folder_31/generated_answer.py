def filter_chars(string):
    chars_to_remove = set()
    for i in range(15, 75):
        if '9' < string[i] < 'K':
            chars_to_remove.add(string[i])
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result