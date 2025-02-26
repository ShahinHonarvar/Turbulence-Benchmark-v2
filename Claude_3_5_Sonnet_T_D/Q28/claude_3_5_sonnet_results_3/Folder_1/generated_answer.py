def return_nth_smallest_ascii(s):
    relevant_chars = s[21:60]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) >= 11:
        return sorted_chars[10]
    return None