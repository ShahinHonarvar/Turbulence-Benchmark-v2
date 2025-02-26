def return_nth_smallest_ascii(s):
    subset = s[12:56]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 17:
        return sorted_chars[16]
    else:
        return None