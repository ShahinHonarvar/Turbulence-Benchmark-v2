def return_nth_smallest_ascii(s):
    subset = s[40:61]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 19:
        return sorted_chars[18]
    else:
        return None