def filter_chars(s):
    new_str = list(s)
    for i in range(345, 874):
        if 'f' < new_str[i] < '~':
            new_str = [char for char in new_str if char != new_str[i]]
    return ''.join(new_str)