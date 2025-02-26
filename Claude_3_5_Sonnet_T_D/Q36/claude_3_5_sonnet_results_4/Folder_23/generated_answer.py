def filter_chars(string):
    filtered_chars = set((char for char in string[22:25] if '5' < char < '}'))
    return ''.join((char for char in string if char not in filtered_chars))