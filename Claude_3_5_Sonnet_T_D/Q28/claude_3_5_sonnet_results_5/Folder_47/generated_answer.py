def return_nth_smallest_ascii(s):
    subset = s[3:53]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 8:
        return sorted_chars[7]
    else:
        return None