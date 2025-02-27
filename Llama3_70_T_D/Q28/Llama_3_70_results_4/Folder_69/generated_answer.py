def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 67 <= i <= 77]
    return sorted(chars, key=ord)[6]