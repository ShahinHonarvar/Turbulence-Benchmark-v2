def filter_chars(input_string):
    for i in range(155, 404):
        if '(' <= input_string[i] <= ']':
            input_string = input_string[:i] + input_string[i + 1:]
    return input_string