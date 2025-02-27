def return_nth_smallest_ascii(s):
    sorted_chars = sorted([c for i, c in enumerate(s) if 46 <= i <= 72], key=lambda c: ord(c))
    return sorted_chars[14]