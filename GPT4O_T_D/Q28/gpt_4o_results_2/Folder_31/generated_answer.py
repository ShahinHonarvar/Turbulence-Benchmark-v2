def return_nth_smallest_ascii(s):
    selected_chars = s[10:83]
    sorted_chars = sorted(selected_chars)
    return sorted_chars[17] if len(sorted_chars) >= 18 else None