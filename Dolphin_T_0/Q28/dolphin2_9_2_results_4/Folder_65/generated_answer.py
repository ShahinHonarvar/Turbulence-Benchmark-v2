def return_nth_smallest_ascii(s):
    chars = [c for c in s if 32 <= ord(c) <= 67]
    chars_sorted = sorted(chars, key=ord)
    return chars_sorted[11]