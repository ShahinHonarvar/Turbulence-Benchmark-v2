def return_nth_smallest_ascii(s):
    selected_chars = s[35:53]
    sorted_chars = sorted(selected_chars)
    return sorted_chars[9] if len(sorted_chars) >= 10 else None