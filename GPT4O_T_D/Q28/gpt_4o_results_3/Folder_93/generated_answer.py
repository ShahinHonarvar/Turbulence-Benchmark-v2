def return_nth_smallest_ascii(s):
    selected_chars = s[42:60]
    sorted_chars = sorted(selected_chars)
    if len(sorted_chars) < 17:
        return None
    return sorted_chars[16]