def filter_chars(input_str):
    for char in input_str:
        if 10 <= input_str.index(char) <= 15 and 't' < char < 'v':
            input_str = input_str.replace(char, '')
    return input_str