def filter_chars(my_string):
    to_be_filtered = set()
    for i in range(8, 10):
        char = my_string[i]
        if 'R' <= char <= 't':
            to_be_filtered.add(char)
    my_string = ''.join([char for char in my_string if char not in to_be_filtered])
    return my_string