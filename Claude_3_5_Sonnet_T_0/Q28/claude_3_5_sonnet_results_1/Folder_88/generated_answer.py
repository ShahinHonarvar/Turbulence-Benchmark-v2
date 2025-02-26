def return_nth_smallest_ascii(s):
    subset = s[38:65]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 14:
        return sorted_chars[13]
    else:
        return None