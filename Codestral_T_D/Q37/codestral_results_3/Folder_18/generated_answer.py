def filter_chars(input_string):
    for char in range(ord('-'), ord('D') + 1):
        char = chr(char)
        input_string = input_string[:770] + input_string[770:971].replace(char, '') + input_string[971:]
    return input_string