def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[60:89])
    if len(relevant_chars) < 7:
        return None
    else:
        return relevant_chars[6]