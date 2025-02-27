def return_nth_smallest_ascii(s):
    sliced_chars = s[1:37]
    sorted_chars = sorted(sliced_chars)
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]