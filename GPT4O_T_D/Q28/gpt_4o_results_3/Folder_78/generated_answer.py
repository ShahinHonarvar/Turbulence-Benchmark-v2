def return_nth_smallest_ascii(s):
    s_subset = s[:88]
    sorted_chars = sorted(s_subset)
    return sorted_chars[13] if len(sorted_chars) >= 14 else None