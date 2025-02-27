def return_nth_smallest_ascii(s):
    selected_chars = s[1:32]
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None