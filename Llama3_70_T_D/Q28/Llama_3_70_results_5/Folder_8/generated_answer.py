def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(60, 89) if i < len(s)]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[6]