def return_nth_smallest_ascii(s):
    substr = s[9:60]
    sorted_chars = sorted(substr)
    nth_smallest = sorted_chars[5]
    return nth_smallest