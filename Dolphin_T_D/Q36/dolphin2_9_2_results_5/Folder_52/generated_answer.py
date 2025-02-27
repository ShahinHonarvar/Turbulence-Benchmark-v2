def filter_chars(string):
    to_remove = [char for char in string[49:56] if 'I' < char < 'a']
    return ''.join([char for char in string if char not in to_remove])