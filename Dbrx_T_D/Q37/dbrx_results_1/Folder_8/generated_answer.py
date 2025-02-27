def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 41 or i > 86:
            filtered_string += input_string[i]
        elif input_string[i] >= 'S' and input_string[i] <= 's':
            continue
        else:
            filtered_string += input_string[i]
    return filtered_string