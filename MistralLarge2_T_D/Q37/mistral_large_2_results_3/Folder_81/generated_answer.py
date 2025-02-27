def filter_chars(input_string):
    indices_to_remove = set((input_string[i] for i in range(19, 93) if '8' <= input_string[i] <= 'm'))
    return ''.join((char for char in input_string if char not in indices_to_remove))