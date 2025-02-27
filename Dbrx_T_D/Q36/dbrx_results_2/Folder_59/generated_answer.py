def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i >= 3 and i < 8:
            if ord(input_string[i]) > ord('?') and ord(input_string[i]) < ord('k'):
                continue
        filtered_string += input_string[i]
    return filtered_string