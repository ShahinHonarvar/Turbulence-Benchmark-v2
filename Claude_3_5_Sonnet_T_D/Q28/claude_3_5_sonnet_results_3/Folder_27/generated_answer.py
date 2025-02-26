def return_nth_smallest_ascii(s):
    relevant_chars = s[33:86]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) >= 13:
        return sorted_chars[12]
    else:
        return None