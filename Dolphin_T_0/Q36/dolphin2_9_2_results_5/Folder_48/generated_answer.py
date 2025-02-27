def filter_chars(input_string):
    for c in range(154, 222):
        if 'A' < input_string[c] < 'f':
            new_string = input_string[:c] + input_string[c + 1:]
            input_string = new_string
    return input_string