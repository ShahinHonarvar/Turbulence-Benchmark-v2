def filter_chars(string):
    chars_to_remove = set()
    for i in range(42, 93):
        if '/' <= string[i] <= 'a':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))