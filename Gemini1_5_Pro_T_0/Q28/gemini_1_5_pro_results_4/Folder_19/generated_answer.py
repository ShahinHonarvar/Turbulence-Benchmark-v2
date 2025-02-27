def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[0:19])
    if len(relevant_chars) >= 13:
        return relevant_chars[12]
    else:
        return None