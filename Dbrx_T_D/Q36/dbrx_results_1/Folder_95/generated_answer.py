def filter_chars(input_string: str) -> str:
    start_index = 56
    end_index = 86
    char_threshold_lower = '+'
    char_threshold_upper = 'w'
    result_list = list(input_string)
    for i in range(start_index, end_index):
        if char_threshold_lower < input_string[i] < char_threshold_upper:
            result_list = [char for char in result_list if char != input_string[i]]
    return ''.join(result_list)