def return_nth_smallest_ascii(s):
    subset = s[37:60]
    sorted_chars = sorted(subset, key=lambda x: ord(x))
    if len(sorted_chars) < 6:
        return None
    return sorted_chars[5]