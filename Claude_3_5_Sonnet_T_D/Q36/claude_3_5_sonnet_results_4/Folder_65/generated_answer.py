def filter_chars(string):
    chars_to_remove = set()
    for i in range(59, 82):
        if i < len(string) and 'F' < string[i] < 'O':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))