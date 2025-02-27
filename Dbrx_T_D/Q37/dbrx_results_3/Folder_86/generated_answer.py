def filter_chars(input_string):
    start_index = 164
    end_index = 706
    min_char = 'O'
    max_char = '}'
    for i in range(len(input_string)):
        if start_index <= i <= end_index:
            char = input_string[i]
            if min_char <= char <= max_char:
                input_string = input_string[:i] + input_string[i + 1:]
    return input_string