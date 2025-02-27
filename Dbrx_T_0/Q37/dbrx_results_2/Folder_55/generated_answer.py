def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 1 or i > 5:
            filtered_string += input_string[i]
        elif input_string[i] >= '$' and input_string[i] <= ';':
            continue
        else:
            filtered_string += input_string[i]
    return filtered_string