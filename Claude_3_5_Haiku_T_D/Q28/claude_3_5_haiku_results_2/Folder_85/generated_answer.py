def return_nth_smallest_ascii(s):
    filtered_chars = s[17:87]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[14]