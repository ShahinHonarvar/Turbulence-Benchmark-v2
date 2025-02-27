def return_nth_smallest_ascii(s):
    if len(s) < 9:
        return None
    subset = s[:9]
    sorted_chars = sorted(subset, key=lambda x: ord(x))
    return sorted_chars[8]