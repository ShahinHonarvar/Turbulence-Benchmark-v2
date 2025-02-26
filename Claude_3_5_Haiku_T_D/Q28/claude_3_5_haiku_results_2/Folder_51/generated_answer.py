def return_nth_smallest_ascii(input_string):
    filtered_chars = input_string[10:74]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[8]