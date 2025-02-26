def return_nth_smallest_ascii(input_string):
    subset_chars = input_string[17:87]
    sorted_chars = sorted(subset_chars)
    return sorted_chars[14]