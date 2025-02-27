def filter_chars(input_string):
    new_string = ''
    for i in range(len(input_string)):
        if i >= 56 and i < 86:
            if ord(input_string[i]) > ord('+') and ord(input_string[i]) < ord('w'):
                continue
        new_string += input_string[i]
    return new_string