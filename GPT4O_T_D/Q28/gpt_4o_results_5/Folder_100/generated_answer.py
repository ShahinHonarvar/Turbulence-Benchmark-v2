def return_nth_smallest_ascii(s):
    sliced_string = s[5:48]
    sorted_chars = sorted(sliced_string)
    return sorted_chars[12] if len(sorted_chars) >= 13 else None