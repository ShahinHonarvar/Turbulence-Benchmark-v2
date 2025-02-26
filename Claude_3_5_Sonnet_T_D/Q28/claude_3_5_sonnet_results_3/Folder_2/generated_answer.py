def return_nth_smallest_ascii(s):
    relevant_chars = s[48:77]
    sorted_chars = sorted(relevant_chars)
    if len(sorted_chars) >= 5:
        return sorted_chars[4]
    else:
        return None