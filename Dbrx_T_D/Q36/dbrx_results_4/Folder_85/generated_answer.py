def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i >= 55 and i < 80:
            if ord(input_string[i]) > ord('S') and ord(input_string[i]) < ord('s'):
                continue
        filtered_string += input_string[i]
    return filtered_string