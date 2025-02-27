def filter_chars(input_str):
    start_idx = 11
    end_idx = 32
    char_range = range(ord('!'), ord('@') + 1)
    result = ''
    for i in range(len(input_str)):
        if (i < start_idx or i > end_idx) and ord(input_str[i]) not in char_range:
            result += input_str[i]
    return result