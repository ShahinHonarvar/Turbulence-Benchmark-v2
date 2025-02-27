def return_nth_smallest_ascii(s):
    chars_between_indices = [s[i] for i in range(51, 90)]
    sorted_chars = sorted(chars_between_indices)
    return sorted_chars[13]