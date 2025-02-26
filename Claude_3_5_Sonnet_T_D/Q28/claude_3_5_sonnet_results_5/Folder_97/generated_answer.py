def return_nth_smallest_ascii(s):
    subset = s[15:22]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 6:
        return sorted_chars[5]
    else:
        return None