def return_nth_smallest_ascii(s):
    subset = s[25:78]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 16:
        return sorted_chars[15]
    else:
        return None