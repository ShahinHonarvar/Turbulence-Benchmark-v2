def return_nth_smallest_ascii(s):
    if len(s) <= 88:
        return None
    selected_chars = s[25:89]
    sorted_chars = sorted(selected_chars)
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]