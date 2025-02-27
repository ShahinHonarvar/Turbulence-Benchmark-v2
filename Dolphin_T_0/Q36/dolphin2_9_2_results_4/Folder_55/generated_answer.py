def filter_chars(input_str):
    for i in range(3, 5):
        char = input_str[i]
        if 'Y' < char < 's':
            input_str = input_str.replace(char, '')
    return input_str