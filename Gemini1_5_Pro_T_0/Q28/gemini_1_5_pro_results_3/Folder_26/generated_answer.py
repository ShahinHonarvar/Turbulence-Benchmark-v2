def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[1:37])
    if len(relevant_chars) >= 15:
        return relevant_chars[14]
    else:
        return None