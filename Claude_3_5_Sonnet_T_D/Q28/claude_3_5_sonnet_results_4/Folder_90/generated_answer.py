def return_nth_smallest_ascii(s):
    subset = s[17:84]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 5:
        return sorted_chars[4]
    else:
        return None