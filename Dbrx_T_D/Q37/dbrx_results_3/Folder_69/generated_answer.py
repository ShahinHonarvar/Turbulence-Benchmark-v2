def filter_chars(input_string):
    start_index = 114
    end_index = 639
    char_codes = range(ord('!'), ord('x') + 1)
    for i in range(len(input_string)):
        if start_index <= i <= end_index and ord(input_string[i]) in char_codes:
            input_string = input_string[:i] + input_string[i + 1:]
            i -= 1
    return input_string