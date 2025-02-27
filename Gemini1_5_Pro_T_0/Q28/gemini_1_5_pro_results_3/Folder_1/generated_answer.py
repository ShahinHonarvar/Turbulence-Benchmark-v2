def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[21:60])
    if len(relevant_chars) >= 11:
        return relevant_chars[10]
    else:
        return None