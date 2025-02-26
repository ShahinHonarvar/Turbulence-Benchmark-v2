def filter_chars(string):
    chars_to_remove = set()
    for i in range(421, 854):
        if i < len(string) and 'D' < string[i] < 'J':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))