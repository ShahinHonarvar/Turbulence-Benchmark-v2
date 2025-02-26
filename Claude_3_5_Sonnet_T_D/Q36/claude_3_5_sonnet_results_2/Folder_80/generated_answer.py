def filter_chars(input_string):
    to_remove = set()
    for i in range(55, 92):
        if i < len(input_string):
            if 'J' < input_string[i] < 'X':
                to_remove.add(input_string[i])
    return ''.join((char for char in input_string if char not in to_remove))