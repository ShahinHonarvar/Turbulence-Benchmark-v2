def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 35 or i > 40:
            filtered_string += input_string[i]
        elif input_string[i] >= ')' and input_string[i] <= 'l':
            continue
        else:
            filtered_string += input_string[i]
    return filtered_string