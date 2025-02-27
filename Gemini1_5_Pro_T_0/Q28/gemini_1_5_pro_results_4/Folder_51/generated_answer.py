def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[10:74])
    if len(relevant_chars) >= 9:
        return relevant_chars[8]
    else:
        return None