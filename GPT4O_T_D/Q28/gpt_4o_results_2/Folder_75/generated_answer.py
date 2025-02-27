def return_nth_smallest_ascii(s):
    subset_chars = s[62:84]
    sorted_chars = sorted(subset_chars, key=lambda c: ord(c))
    if len(sorted_chars) < 9:
        return None
    return sorted_chars[8]