def return_nth_smallest_ascii(s):
    subset = s[:46]
    sorted_chars = sorted(set(subset), key=ord)
    return sorted_chars[9] if len(sorted_chars) >= 10 else None