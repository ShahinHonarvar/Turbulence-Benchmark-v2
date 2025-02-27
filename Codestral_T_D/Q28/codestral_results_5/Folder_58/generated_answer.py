def return_nth_smallest_ascii(string):
    sorted_chars = sorted(string[8:27], key=ord)
    return sorted_chars[5]