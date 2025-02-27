def filter_chars(input_string):
    for i in range(len(input_string)):
        if 90 < i < 97:
            char_at_index = input_string[i]
            if ord('j') < ord(char_at_index) < ord('w'):
                input_string = input_string.replace(char_at_index, '', 1)
    return input_string