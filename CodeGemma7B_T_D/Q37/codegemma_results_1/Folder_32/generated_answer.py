def filter_chars(some_string):
    """
    some_string: str
    """
    filtered_string = ''
    for i in range(len(some_string)):
        if i < 23 or i > 89 or (some_string[i] < 'w' or some_string[i] > '{'):
            filtered_string += some_string[i]
    return filtered_string