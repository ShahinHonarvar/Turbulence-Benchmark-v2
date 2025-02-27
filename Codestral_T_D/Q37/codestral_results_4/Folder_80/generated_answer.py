def filter_chars(input_string):
    for char in sorted(set(input_string[36:80])):
        if 'a' <= char <= 'i':
            input_string = input_string.replace(char, '')
    return input_string