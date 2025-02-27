def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i >= 154 and i < 222:
            if input_string[i] > 'A' and input_string[i] < 'f':
                continue
        filtered_string += input_string[i]
    return filtered_string