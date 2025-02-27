def return_nth_smallest_ascii(s):
    if len(s) < 91:
        return None
    relevant_chars = s[10:91]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) < 20:
        return None
    return sorted_chars[19]