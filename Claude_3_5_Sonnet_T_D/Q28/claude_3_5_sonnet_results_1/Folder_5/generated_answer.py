def return_nth_smallest_ascii(s):
    subset = s[5:90]
    sorted_chars = sorted(set(subset), key=ord)
    if len(sorted_chars) >= 13:
        return sorted_chars[12]
    return None