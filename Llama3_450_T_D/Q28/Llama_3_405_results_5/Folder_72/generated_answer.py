def return_nth_smallest_ascii(s):
    section = s[33:61]
    unique_chars = sorted(set(section))
    if len(unique_chars) < 18:
        return None
    else:
        return unique_chars[17]