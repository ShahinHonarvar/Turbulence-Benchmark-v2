def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[60:84])
    if len(relevant_chars) >= 14:
        return relevant_chars[13]
    else:
        return None