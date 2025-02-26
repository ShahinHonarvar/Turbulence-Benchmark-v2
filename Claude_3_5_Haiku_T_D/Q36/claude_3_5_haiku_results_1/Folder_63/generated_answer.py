def filter_chars(string):
    chars_to_remove = set()
    for i in range(26, 80):
        if '<' < string[i] < '>':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))