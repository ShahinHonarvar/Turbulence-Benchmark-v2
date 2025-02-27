def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(62, 84) if 62 <= i <= 83]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[8]