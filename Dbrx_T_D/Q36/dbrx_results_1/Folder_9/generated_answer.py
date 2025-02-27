def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i >= 50 and i < 92:
            if input_string[i] > 'A' and input_string[i] < 'Q':
                input_string = input_string[:i] + input_string[i + 1:]
        filtered_string += input_string[i]
    return filtered_string