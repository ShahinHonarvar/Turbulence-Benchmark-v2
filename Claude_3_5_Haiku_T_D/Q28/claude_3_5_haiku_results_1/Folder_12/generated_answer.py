def return_nth_smallest_ascii(input_string):
    selected_chars = input_string[3:27]
    sorted_chars = sorted(selected_chars)
    return sorted_chars[4]