def filter_chars(string):
    chars_to_remove = set()
    for i in range(52, 76):
        if '5' < string[i] < 'f':
            chars_to_remove.add(string[i])
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result