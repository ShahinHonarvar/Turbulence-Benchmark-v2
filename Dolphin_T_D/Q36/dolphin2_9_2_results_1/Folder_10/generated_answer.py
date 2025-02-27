def filter_chars(input_string):
    for i in range(35, 60):
        char = input_string[i]
        if char > '!' and char < 'B':
            input_string = input_string.replace(char, '')
    return input_string