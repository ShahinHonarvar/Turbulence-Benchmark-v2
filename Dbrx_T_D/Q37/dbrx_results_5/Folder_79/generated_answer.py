def filter_chars(input_string):
    result_string = ''
    for i in range(len(input_string)):
        if i < 10 or i > 52 or ord(input_string[i]) < ord('@') or (ord(input_string[i]) > ord('T')):
            result_string += input_string[i]
    return result_string