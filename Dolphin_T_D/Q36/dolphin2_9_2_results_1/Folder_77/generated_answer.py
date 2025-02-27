def filter_chars(input_string):
    remove_chars = []
    for i in range(221, 419):
        if input_string[i] > '-' and input_string[i] < 'v':
            remove_chars.append(input_string[i])
    for r_char in remove_chars:
        input_string = input_string.replace(r_char, '')
    return input_string