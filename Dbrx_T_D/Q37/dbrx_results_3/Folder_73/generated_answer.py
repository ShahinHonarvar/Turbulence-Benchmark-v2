def filter_chars(input_string):
    start_index = 22
    end_index = 85
    char_set = set(range(ord('7'), ord('e') + 1))
    filtered_chars = [char for i, char in enumerate(input_string) if (i < start_index or i > end_index) or char not in char_set]
    return ''.join(filtered_chars)