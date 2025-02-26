def return_nth_smallest_ascii(string):
    selected_chars = string[:19]
    sorted_chars = sorted(selected_chars)
    return sorted_chars[12]