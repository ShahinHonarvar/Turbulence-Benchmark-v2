def return_nth_smallest_ascii(s):
    chars_between_indices = [c for i, c in enumerate(s) if 62 <= i <= 83]
    sorted_chars = sorted(chars_between_indices, key=lambda x: ord(x))
    return sorted_chars[8]