def filter_chars(input_string):
    result_string = ''
    for i in range(len(input_string)):
        if i < 18 or i >= 95:
            result_string += input_string[i]
        elif input_string[i] > 'K' and input_string[i] < 'a':
            continue
        else:
            result_string += input_string[i]
    return result_string