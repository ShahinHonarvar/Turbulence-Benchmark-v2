def filter_chars(input_str):
    start_index = 154
    end_index = 222
    char_set = set((chr(i) for i in range(ord('A'), ord('f') + 1)))
    filtered_chars = [c for c in input_str[start_index:end_index] if c not in char_set]
    return input_str[:start_index] + ''.join(filtered_chars) + input_str[end_index:]