def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 259 or i > 502:
            filtered_string += input_string[i]
        elif ord(input_string[i]) >= ord(',') and ord(input_string[i]) <= ord('3'):
            continue
        else:
            filtered_string += input_string[i]
    return filtered_string