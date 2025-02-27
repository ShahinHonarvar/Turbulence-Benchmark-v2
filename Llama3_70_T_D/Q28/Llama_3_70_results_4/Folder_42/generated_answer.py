def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(12, 73)]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[12]