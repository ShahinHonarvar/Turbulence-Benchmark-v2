def filter_chars(input_string):
    result_string = ''
    for i in range(len(input_string)):
        if i < 24 or i > 79 or ord(input_string[i]) < ord('a') or (ord(input_string[i]) > ord('f')):
            result_string += input_string[i]
    return result_string