def return_nth_smallest_ascii(s):
    chars_between_20_30 = [c for i, c in enumerate(s) if 20 <= i <= 30]
    sorted_chars = sorted(chars_between_20_30, key=lambda x: ord(x))
    return sorted_chars[7]