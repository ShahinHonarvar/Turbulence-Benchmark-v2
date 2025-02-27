def return_nth_smallest_ascii(s):
    selected_chars = s[17:35]
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[17] if len(sorted_chars) >= 18 else None