def filter_chars(input_string):
    for i in range(770, 970):
        char_at_index = input_string[i]
        if '-D'.find(char_at_index) != -1:
            input_string = input_string[:i] + input_string[i + 1:]
    return input_string