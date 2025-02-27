def filter_chars(input_string):
    start_index = 2
    end_index = 3
    char_range = range(ord('5'), ord('_') + 1)
    result = ''
    for i in range(len(input_string)):
        if i < start_index or i > end_index or ord(input_string[i]) not in char_range:
            result += input_string[i]
    return result