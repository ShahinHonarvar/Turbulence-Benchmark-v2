def return_nth_smallest_ascii(s):
    subset = s[18:67]
    sorted_chars = sorted(subset)
    if len(sorted_chars) >= 19:
        return sorted_chars[18]
    return None