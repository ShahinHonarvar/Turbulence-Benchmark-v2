def return_nth_smallest_ascii(input_str):
    sorted_chars = sorted(input_str[1:36], key=lambda x: ord(x))
    return sorted_chars[14]