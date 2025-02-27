def filter_chars(input_str):
    start_index = 23
    end_index = 45
    char_set = set(range(ord('3') + 1, ord('I')))
    filtered_chars = [c for c in input_str if c < '3' or c > 'I' or ord(c) not in char_set][start_index:end_index]
    return ''.join(filtered_chars)