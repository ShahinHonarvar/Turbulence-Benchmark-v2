def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=ord)
    result = sorted_chars[:85] if len(sorted_chars) >= 85 else sorted_chars + [chr(0)] * (85 - len(sorted_chars))
    return sorted(result, reverse=True)