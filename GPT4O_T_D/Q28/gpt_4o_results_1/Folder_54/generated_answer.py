def return_nth_smallest_ascii(s):
    filtered_chars = s[12:88]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[16] if len(sorted_chars) >= 17 else None