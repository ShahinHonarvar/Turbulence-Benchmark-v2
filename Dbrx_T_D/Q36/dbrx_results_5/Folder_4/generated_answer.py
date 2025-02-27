def filter_chars(input_string: str) -> str:
    start_index = 42
    end_index = 65
    char_threshold_lower = '6'
    char_threshold_upper = 'g'
    chars_to_remove = set()
    for char in input_string[start_index:end_index]:
        if char_threshold_lower < char < char_threshold_upper:
            chars_to_remove.add(char)
    for char in chars_to_remove:
        input_string = input_string.replace(char, '', 1)
    return input_string