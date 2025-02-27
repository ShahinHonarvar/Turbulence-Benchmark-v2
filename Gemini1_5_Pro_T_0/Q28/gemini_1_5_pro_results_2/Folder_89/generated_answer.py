def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[24:72])
    if len(relevant_chars) >= 8:
        return relevant_chars[7]
    else:
        return None