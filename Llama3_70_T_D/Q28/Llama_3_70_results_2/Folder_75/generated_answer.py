def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(62, 84) if s[i] in s]
    sorted_chars = sorted(set(chars_in_range))
    return sorted_chars[8]