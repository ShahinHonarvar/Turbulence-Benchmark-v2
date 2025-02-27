def return_nth_smallest_ascii(s):
    unique_chars = sorted(list(set(s[0:7])))
    if len(unique_chars) >= 7:
        return unique_chars[6]
    else:
        return None