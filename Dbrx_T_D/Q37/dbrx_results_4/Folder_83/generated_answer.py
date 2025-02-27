def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 29 or i > 79:
            filtered_string += input_string[i]
        elif input_string[i] < 'K' or input_string[i] > 'z':
            filtered_string += input_string[i]
        continue
    return filtered_string