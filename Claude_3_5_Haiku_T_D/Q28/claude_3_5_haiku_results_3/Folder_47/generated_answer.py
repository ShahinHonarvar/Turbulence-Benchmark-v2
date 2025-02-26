def return_nth_smallest_ascii(string):
    filtered_chars = string[3:53]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[7]