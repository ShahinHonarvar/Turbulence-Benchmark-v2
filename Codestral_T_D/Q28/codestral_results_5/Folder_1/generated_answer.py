def return_nth_smallest_ascii(s):
    substring = s[21:60]
    sorted_chars = sorted(substring)
    nth_smallest_char = sorted_chars[10]
    return nth_smallest_char