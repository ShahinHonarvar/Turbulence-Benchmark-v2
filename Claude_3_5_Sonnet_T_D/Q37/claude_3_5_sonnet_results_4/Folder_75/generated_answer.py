def filter_chars(input_string):
    characters_to_remove = set()
    for i in range(34, 68):
        if i < len(input_string):
            if 'W' <= input_string[i] <= 'x':
                characters_to_remove.add(input_string[i])
    result = ''.join((char for char in input_string if char not in characters_to_remove))
    return result