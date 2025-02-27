def filter_chars(input_string):
    for char in range(ord('K') + 1, ord('a') - 1):
        input_string = input_string.replace(chr(char), '')
    return input_string