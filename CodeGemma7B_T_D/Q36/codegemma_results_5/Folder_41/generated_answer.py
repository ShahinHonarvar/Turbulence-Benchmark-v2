def filter_chars(str):
    return ''.join([i for i in str if i < 'f' or i > '{'])