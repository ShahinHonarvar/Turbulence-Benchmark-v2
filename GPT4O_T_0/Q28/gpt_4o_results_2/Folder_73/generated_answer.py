def return_nth_smallest_ascii(s):
    if len(s) < 70:
        s = s[:len(s)]
    else:
        s = s[:70]
    sorted_chars = sorted(s)
    return sorted_chars[9] if len(sorted_chars) >= 10 else None