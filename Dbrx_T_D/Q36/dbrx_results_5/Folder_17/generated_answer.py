def filter_chars(string):
    filter_func = lambda char: 'K' < char < 'a'
    return ''.join((char for char in string if not filter_func(char)))[18:95]