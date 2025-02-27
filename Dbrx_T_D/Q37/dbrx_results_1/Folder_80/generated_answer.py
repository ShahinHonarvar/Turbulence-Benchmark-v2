def filter_chars(input_string):
    for i in range(len(input_string)):
        if 36 <= i <= 79 and 'a' <= input_string[i] <= 'i':
            input_string = input_string[:i] + input_string[i + 1:]
    return input_string