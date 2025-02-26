def return_nth_smallest_ascii(s):
    relevant_chars = s[12:88]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[16] if len(sorted_chars) >= 17 else None