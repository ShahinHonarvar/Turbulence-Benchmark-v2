def return_nth_smallest_ascii(s):
    filtered_chars = s[5:48]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[12] if len(sorted_chars) >= 13 else None