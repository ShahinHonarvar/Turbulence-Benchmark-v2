def return_nth_smallest_ascii(s):
    chars_in_range = [s[i] for i in range(12, 88) if 12 <= i <= 87]
    sorted_chars = sorted(chars_in_range, key=lambda c: ord(c))
    return sorted_chars[16]