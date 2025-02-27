def return_nth_smallest_ascii(input_string):
    chars_in_range = [input_string[i] for i in range(17, 87) if input_string[i] != '']
    chars_in_range.sort(key=ord)
    return chars_in_range[14] if len(chars_in_range) >= 15 else None