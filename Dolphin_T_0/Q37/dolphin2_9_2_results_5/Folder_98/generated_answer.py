def filter_chars(input_str):
    for index in range(len(input_str)):
        if 8 <= index <= 9:
            for char in input_str:
                if 'R' <= char <= 't':
                    input_str = input_str.replace(char, '')
    return input_str