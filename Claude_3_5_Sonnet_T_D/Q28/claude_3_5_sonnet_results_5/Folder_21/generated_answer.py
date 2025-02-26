def return_nth_smallest_ascii(s):
    subset = s[8:66]
    sorted_chars = sorted(set(subset), key=ord)
    return sorted_chars[5] if len(sorted_chars) > 5 else None