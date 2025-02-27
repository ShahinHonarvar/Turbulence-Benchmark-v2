def filter_chars(input_string):
    result_string = ''
    for i in range(len(input_string)):
        if i < 20 or i > 79:
            result_string += input_string[i]
        elif input_string[i] >= '!' and input_string[i] <= 'T':
            continue
        else:
            result_string += input_string[i]
    return result_string