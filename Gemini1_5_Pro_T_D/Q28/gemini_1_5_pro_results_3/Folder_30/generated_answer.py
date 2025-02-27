def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[50:77])
    if len(relevant_chars) >= 11:
        return relevant_chars[10]
    else:
        return None