def filter_chars(string):
    chars_to_remove = set()
    for i in range(41, 63):
        if '7' < string[i] < 'H':
            chars_to_remove.add(string[i])
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result