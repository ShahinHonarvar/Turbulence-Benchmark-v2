def return_nth_smallest_ascii(s):
    if len(s) < 89:
        return None
    relevant_chars = s[60:89]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[6]