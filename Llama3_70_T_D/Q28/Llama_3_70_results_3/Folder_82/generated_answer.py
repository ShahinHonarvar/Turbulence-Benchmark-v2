def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if i <= 14]
    return sorted(chars, key=ord)[14]