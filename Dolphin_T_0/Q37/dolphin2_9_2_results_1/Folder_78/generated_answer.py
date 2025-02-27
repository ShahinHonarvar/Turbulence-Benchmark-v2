def filter_chars(input_string):
    altered_string = ''
    preserve_order = True
    for index, char in enumerate(input_string):
        if 75 <= index <= 99 and '8' <= char <= 'e':
            input_string = input_string.replace(char, '')
    return input_string