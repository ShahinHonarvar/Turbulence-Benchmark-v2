def filter_chars(input_string):
    start_index = 227
    end_index = 235
    char_set = set(range(ord('D'), ord('u') + 1))
    filtered_chars = []
    for i, char in enumerate(input_string):
        if i < start_index or i > end_index or ord(char) not in char_set:
            filtered_chars.append(char)
    return ''.join(filtered_chars)