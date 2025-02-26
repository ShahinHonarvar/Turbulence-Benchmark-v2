def return_nth_smallest_ascii(s):
    filtered_chars = s[:46]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[9]