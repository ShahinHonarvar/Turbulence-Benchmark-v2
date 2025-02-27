def filter_chars(input_string: str) -> str:
    start_index = 68
    end_index = 97
    char_threshold_upper = 'V'
    char_threshold_lower = 'j'
    for i in range(start_index, end_index):
        char = input_string[i]
        if char_threshold_lower < char < char_threshold_upper:
            input_string = input_string.replace(char, '', 1)
    return input_string