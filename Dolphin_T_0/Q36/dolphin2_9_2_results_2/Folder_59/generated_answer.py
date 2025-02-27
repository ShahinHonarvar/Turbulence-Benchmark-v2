def filter_chars(input_str):
    for char in input_str:
        if ord('?') < ord(char) < ord('k'):
            input_str = input_str.replace(char, '')
    return input_str