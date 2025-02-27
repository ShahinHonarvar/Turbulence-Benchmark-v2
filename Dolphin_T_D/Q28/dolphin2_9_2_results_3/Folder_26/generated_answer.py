def return_nth_smallest_ascii(s):
    chars = sorted([c for c in s[:37] if 1 <= s.index(c) <= 36])
    return chars[14]