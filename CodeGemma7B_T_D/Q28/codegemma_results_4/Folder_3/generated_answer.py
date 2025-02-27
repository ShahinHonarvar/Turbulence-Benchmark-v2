def return_nth_smallest_ascii(input_string):
    target_chars = input_string[25:46]
    sorted_chars = sorted(target_chars)
    return sorted_chars[10]