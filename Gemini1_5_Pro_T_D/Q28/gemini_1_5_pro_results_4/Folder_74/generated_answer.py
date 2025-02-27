def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[1:32])
    if len(relevant_chars) >= 6:
        return relevant_chars[5]
    else:
        return None