def filter_chars(string):
    chars_to_remove = set()
    for i in range(50, 56):
        if i < len(string) and 'I' < string[i] < 'a':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))