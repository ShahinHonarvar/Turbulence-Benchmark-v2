def return_nth_smallest_ascii(s):
    substring = s[40:61]
    sorted_chars = sorted(set(substring))
    return sorted_chars[18]