def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 69 or i > 80 or (i >= 69 and i <= 80 and (not (input_string[i] >= '@' and input_string[i] <= 'p'))):
            filtered_string += input_string[i]
    return filtered_string