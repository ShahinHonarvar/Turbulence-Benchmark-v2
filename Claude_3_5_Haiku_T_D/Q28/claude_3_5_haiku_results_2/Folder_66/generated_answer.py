def return_nth_smallest_ascii(string):
    filtered_chars = [char for char in string[35:53]]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[9]