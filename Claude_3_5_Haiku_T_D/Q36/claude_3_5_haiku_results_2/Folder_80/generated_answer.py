def filter_chars(string):
    chars_to_remove = set()
    for i in range(55, 92):
        if 'J' < string[i] < 'X':
            chars_to_remove.add(string[i])
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result