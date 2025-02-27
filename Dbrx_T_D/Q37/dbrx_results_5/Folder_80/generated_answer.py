def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 36 or i > 79:
            filtered_string += input_string[i]
        elif input_string[i] >= 'a' and input_string[i] <= 'i':
            filtered_string += input_string[i]
    return filtered_string