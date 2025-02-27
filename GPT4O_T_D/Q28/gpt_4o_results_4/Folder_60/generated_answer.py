def return_nth_smallest_ascii(s):
    subset = s[36:80]
    if len(subset) < 12:
        return None
    sorted_chars = sorted(subset)
    return sorted_chars[11]