def filter_chars(input_string):
    filtered_string = ''
    lower_bound = 12
    upper_bound = 88
    lower_char_bound = '&'
    upper_char_bound = 'v'
    for i in range(len(input_string)):
        if i < lower_bound or i > upper_bound:
            filtered_string += input_string[i]
        elif ord(input_string[i]) >= ord(lower_char_bound) and ord(input_string[i]) <= ord(upper_char_bound):
            continue
        else:
            filtered_string += input_string[i]
    return filtered_string