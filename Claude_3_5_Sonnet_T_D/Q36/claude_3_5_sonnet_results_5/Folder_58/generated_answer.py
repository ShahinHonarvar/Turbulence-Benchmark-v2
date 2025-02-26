def filter_chars(input_string):
    characters_to_remove = set()
    for i in range(318, 337):
        if i < len(input_string) and 'B' < input_string[i] < 'z':
            characters_to_remove.add(input_string[i])
    return ''.join((char for char in input_string if char not in characters_to_remove))