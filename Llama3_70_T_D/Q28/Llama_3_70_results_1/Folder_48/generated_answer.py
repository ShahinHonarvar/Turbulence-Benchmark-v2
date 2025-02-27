def return_nth_smallest_ascii(s):
    chars_between_indices = [s[i] for i in range(37, 60)]
    sorted_chars = sorted(chars_between_indices)
    sixth_smallest_ascii = sorted_chars[5]
    return sixth_smallest_ascii