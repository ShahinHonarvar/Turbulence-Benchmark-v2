def return_nth_smallest_ascii(s):
    subset = s[17:87]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 15:
        return sorted_chars[14]
    else:
        return None