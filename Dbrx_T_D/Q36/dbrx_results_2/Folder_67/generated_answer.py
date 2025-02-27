def filter_chars(input_string):
    start_index = 18
    end_index = 31
    min_char = 'H'
    max_char = '|'
    chars_to_remove = set()
    for i in range(start_index, end_index):
        if input_string[i] > min_char and input_string[i] < max_char:
            chars_to_remove.add(input_string[i])
    result = ''
    for char in input_string:
        if char not in chars_to_remove:
            result += char
    return result