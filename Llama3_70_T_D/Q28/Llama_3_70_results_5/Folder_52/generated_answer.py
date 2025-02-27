def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(46, 73) if i < len(s)]
    sorted_chars = sorted(chars_in_range, key=ord)
    return sorted_chars[14]