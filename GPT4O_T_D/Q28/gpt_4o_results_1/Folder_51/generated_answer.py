def return_nth_smallest_ascii(s):
    filtered_chars = s[10:74]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[8] if len(sorted_chars) >= 9 else None