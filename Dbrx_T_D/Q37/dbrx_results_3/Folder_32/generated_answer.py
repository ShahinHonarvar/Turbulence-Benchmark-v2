def filter_chars(input_string):
    result_string = ''
    for i in range(len(input_string)):
        if i < 23 or i > 89 or ord(input_string[i]) < ord('w') or (ord(input_string[i]) > ord('{')):
            result_string += input_string[i]
    return result_string