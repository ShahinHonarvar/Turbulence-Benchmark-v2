def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 13 <= i <= 35]
    char_sorted_by_ascii = sorted(chars, key=lambda c: ord(c))
    return char_sorted_by_ascii[17]