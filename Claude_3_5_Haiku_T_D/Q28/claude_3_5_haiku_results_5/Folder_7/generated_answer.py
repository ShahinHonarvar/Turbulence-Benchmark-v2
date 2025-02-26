def return_nth_smallest_ascii(string):
    filtered_chars = string[12:56]
    sorted_chars = sorted(set(filtered_chars))
    return sorted_chars[16]