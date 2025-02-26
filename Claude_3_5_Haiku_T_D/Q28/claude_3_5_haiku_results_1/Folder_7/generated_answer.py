def return_nth_smallest_ascii(string):
    selected_chars = string[12:56]
    sorted_chars = sorted(selected_chars)
    return sorted_chars[16]