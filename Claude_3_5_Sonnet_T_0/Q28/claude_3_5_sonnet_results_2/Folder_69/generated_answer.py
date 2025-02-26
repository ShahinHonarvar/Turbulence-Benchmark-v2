def return_nth_smallest_ascii(s):
    subset = s[67:78]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 7:
        return sorted_chars[6]
    else:
        return None