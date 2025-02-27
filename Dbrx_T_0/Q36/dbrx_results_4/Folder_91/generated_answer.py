def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if i >= 0 and i < 3:
            if ord(input_string[i]) > ord('$') and ord(input_string[i]) < ord('?'):
                continue
        result += input_string[i]
    return result