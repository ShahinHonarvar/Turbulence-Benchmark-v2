def return_nth_smallest_ascii(s):
    subset = s[50:76]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 7:
        return sorted_chars[6]
    else:
        return None