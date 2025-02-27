def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(51, 61) if 51 <= i <= 60]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[4]