def return_nth_smallest_ascii(s):
    selected_chars = s[58:86]
    selected_chars_sorted = sorted(selected_chars)
    return selected_chars_sorted[18] if len(selected_chars_sorted) > 18 else None