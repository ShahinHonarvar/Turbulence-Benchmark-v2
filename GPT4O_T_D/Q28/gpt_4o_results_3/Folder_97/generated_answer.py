def return_nth_smallest_ascii(s):
    relevant_chars = s[15:22]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) >= 6:
        return sorted_chars[5]
    return None