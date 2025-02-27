def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if not (i >= 603 and i <= 759 and (input_string[i] >= 'Q') and (input_string[i] <= 'h')):
            result += input_string[i]
    return result