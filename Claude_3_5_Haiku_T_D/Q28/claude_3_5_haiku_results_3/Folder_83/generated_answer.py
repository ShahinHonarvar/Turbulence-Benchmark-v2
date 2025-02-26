def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[30:71]]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[14]