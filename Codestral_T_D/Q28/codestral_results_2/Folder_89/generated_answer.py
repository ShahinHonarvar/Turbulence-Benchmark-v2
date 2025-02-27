def return_nth_smallest_ascii(input_str):
    sub_str = input_str[24:72]
    sorted_chars = sorted(sub_str)
    return sorted_chars[7]