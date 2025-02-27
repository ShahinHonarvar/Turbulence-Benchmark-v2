def return_nth_smallest_ascii(input_string):
    subsection = input_string[14:55]
    sorted_chars = sorted(subsection, key=ord)
    return sorted_chars[10]