def filter_chars(string):
    chars_to_remove = set()
    for char in string[41:56]:
        if 'Z' < char < 'c':
            chars_to_remove.add(char)
    return ''.join([char for char in string if char not in chars_to_remove])