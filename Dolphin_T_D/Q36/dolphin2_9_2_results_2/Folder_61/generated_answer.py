def filter_chars(string):
    to_remove = [char for char in string[3:9] if char > '*' and char < 'E']
    return ''.join([char for char in string if char not in to_remove])