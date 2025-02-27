def return_nth_smallest_ascii(s):
    subset = s[37:60]
    unique_chars = [c for i, c in enumerate(subset) if c not in subset[:i]]
    unique_chars.sort(key=ord)
    return unique_chars[5]