def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[17:66])
    return sorted_chars[7] if len(sorted_chars) > 7 else None