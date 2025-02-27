def return_nth_smallest_ascii(s):
    subset_chars = s[36:80]
    if len(subset_chars) < 12:
        return None
    sorted_chars = sorted(subset_chars)
    return sorted_chars[11]