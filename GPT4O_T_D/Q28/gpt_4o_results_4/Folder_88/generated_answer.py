def return_nth_smallest_ascii(s):
    selected_chars = s[38:65]
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None