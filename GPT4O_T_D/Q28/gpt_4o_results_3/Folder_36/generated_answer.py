def return_nth_smallest_ascii(s):
    selected_chars = s[17:57]
    sorted_chars = sorted(selected_chars)
    return sorted_chars[8] if len(sorted_chars) >= 9 else None