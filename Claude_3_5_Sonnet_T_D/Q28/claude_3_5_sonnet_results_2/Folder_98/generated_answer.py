def return_nth_smallest_ascii(s):
    relevant_chars = s[:9]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) >= 9:
        return sorted_chars[8]
    else:
        return None