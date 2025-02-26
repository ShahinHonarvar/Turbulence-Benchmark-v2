def return_nth_smallest_ascii(s):
    selected_chars = s[1:67]
    sorted_chars = sorted(selected_chars)
    return sorted_chars[7]