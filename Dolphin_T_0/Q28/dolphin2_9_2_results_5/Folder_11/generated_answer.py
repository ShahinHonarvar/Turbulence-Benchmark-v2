def return_nth_smallest_ascii(s):
    chars = s[9:60]
    ascii_values = [ord(c) for c in chars]
    sorted_chars = list((c for _, c in sorted(zip(ascii_values, chars))))
    return sorted_chars[5]