def filter_chars(input_string):
    new_string = ''
    for i in range(len(input_string)):
        if i >= 7 and i <= 8 and (input_string[i] >= 'B') and (input_string[i] <= 'H'):
            continue
        else:
            new_string += input_string[i]
    return new_string