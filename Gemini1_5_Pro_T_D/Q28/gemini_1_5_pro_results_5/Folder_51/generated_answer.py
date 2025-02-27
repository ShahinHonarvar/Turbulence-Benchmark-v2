def return_nth_smallest_ascii(string):
    relevant_chars = string[10:74]
    sorted_chars = sorted(relevant_chars, key=ord)
    return sorted_chars[8]