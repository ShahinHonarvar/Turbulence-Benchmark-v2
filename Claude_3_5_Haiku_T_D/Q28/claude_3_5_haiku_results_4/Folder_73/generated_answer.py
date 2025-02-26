def return_nth_smallest_ascii(string):
    filtered_chars = string[:70]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[9]