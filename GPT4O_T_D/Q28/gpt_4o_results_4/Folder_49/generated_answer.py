def return_nth_smallest_ascii(s):
    chars_in_range = s[20:81]
    sorted_chars = sorted(chars_in_range)
    if len(sorted_chars) >= 11:
        return sorted_chars[10]
    return None