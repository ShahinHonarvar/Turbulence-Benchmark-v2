def filter_chars(string):
    chars_to_remove = [char for char in string[23:45] if '3' < char < 'I']
    return ''.join((char for char in string if char not in chars_to_remove))