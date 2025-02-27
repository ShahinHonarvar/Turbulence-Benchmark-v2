def filter_chars(input_string):
    start_index = 37
    end_index = 56
    chars_to_remove = [chr(i) for i in range(ord('6'), ord('_') + 1)]
    filtered_chars = [char for index, char in enumerate(input_string) if index < start_index or index > end_index or char not in chars_to_remove]
    return ''.join(filtered_chars)