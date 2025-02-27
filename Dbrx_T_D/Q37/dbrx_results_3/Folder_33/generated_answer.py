def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 722 or i > 832:
            filtered_string += input_string[i]
        elif input_string[i] < 'K' or input_string[i] > 'm':
            filtered_string += input_string[i]
    return filtered_string