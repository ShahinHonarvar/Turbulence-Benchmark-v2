def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 30 <= i <= 70]
    sorted_chars = sorted(chars, key=lambda c: ord(c))
    return sorted_chars[14]