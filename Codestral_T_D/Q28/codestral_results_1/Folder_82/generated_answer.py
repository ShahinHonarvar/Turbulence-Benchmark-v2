def return_nth_smallest_ascii(s):
    if len(s) <= 14:
        return None
    sorted_chars = sorted(s[:15], key=ord)
    return sorted_chars[14]