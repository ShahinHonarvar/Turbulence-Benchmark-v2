def return_nth_smallest_ascii(s):
    selected_chars = s[0:4]
    sorted_chars = sorted(selected_chars)
    return sorted_chars[3]