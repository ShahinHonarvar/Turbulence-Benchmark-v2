def filter_chars(string):
    chars_to_remove = set()
    for char in string[40:63]:
        if '7' < char < 'H':
            chars_to_remove.add(char)
    return ''.join([char for char in string if char not in chars_to_remove])