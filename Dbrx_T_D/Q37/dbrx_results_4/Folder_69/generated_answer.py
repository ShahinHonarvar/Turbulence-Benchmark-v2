def filter_chars(input_string):
    for i in range(len(input_string)):
        if ord('!') <= ord(input_string[i]) <= ord('x') and 114 <= i < 639:
            input_string = input_string[:i] + input_string[i + 1:]
    return input_string