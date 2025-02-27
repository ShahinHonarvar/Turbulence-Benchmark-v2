def filter_chars(string):
    removed_chars = [char for char, index in zip(string, range(46, 68)) if char > 'H' and char < 's']
    return ''.join([char for char in string if char not in removed_chars])