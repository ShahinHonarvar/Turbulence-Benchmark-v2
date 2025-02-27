def filter_chars(s):
    to_remove = [char for char in s[769:971] if '-' <= char <= 'D']
    new_string = ''.join((char for char in s if char not in to_remove))
    return new_string