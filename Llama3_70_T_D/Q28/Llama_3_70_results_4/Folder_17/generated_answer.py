def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(4, 34) if i < len(s)]
    sorted_chars_in_range = sorted(chars_in_range)
    return sorted_chars_in_range[3]