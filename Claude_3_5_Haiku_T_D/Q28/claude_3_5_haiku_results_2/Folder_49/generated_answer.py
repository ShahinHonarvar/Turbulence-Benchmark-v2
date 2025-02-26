def return_nth_smallest_ascii(s):
    chars_in_range = [char for char in s[20:81]]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[10]