def return_nth_smallest_ascii(s):
    chars_between_indices = [c for i, c in enumerate(s) if 60 <= i <= 88]
    sorted_chars = sorted(chars_between_indices, key=lambda c: ord(c))
    return sorted_chars[6]