def filter_chars(input_string):
    for i in range(len(input_string)):
        if 155 <= i <= 403 and ord('(') <= ord(input_string[i]) <= ord(']'):
            input_string = input_string[:i] + input_string[i + 1:]
    return input_string