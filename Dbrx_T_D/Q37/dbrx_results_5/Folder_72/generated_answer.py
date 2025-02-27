def filter_chars(input_str):
    for index in range(35, 52):
        if 'H' <= input_str[index] <= 's':
            input_str = ''.join((char for char in input_str if char != input_str[index]))
    return input_str