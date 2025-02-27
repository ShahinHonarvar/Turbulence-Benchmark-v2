def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[25:78])
    if len(relevant_chars) < 16:
        return None
    return relevant_chars[15]