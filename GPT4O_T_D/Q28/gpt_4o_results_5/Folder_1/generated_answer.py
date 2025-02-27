def return_nth_smallest_ascii(s):
    filtered_chars = s[21:60]
    ascii_sorted_chars = sorted(filtered_chars, key=ord)
    return ascii_sorted_chars[10] if len(ascii_sorted_chars) >= 11 else None