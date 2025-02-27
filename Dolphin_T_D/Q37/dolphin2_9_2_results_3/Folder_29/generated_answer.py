def filter_chars(input_str):
    for char in input_str:
        if 12 <= input_str.index(char) <= 88 and '&' <= char <= 'v':
            input_str = input_str.replace(char, '')
    return input_str