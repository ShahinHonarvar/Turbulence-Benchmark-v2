def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[34:86])
    if len(relevant_chars) < 20:
        return None
    else:
        return relevant_chars[19]