def return_nth_smallest_ascii(s):
    if len(s) < 9:
        return None
    selected_chars = s[8:66]
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None