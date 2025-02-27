def return_nth_smallest_ascii(string):
    filtered_chars = string[10:91]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[19]