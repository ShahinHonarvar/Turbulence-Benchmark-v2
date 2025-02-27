def filter_chars(input_string):
    for i in range(30, 34):
        for char in input_string[i]:
            if ord('%') < ord(char) < ord('a'):
                input_string = input_string.replace(char, '')
    return input_string