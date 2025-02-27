def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 51 <= i <= 60]
    return sorted(chars, key=ord)[4]