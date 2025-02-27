def return_nth_smallest_ascii(s):
    selected_chars = s[3:27]
    sorted_chars = sorted(selected_chars)
    return sorted_chars[4] if len(sorted_chars) >= 5 else None