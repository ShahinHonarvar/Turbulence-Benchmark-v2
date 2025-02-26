def return_nth_smallest_ascii(s):
    relevant_chars = s[:88]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) >= 14:
        return sorted_chars[13]
    else:
        return None