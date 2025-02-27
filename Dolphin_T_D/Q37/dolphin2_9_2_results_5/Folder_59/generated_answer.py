def filter_chars(input_str):
    for i in range(2, 4):
        for char in input_str[i]:
            if 5 <= ord(char) <= ord('_'):
                input_str = input_str.replace(char, '')
    return input_str