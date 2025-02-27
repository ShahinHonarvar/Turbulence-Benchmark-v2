def return_nth_smallest_ascii(s):
    subsection = s[14:55]
    sorted_chars = sorted(subsection)
    if len(sorted_chars) >= 11:
        return sorted_chars[10]
    return None