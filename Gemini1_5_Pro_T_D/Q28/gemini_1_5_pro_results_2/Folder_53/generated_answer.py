def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[40:61])
    if len(relevant_chars) >= 19:
        return relevant_chars[18]
    else:
        return None