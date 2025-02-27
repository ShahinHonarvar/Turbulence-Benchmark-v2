def return_nth_smallest_ascii(s):
    chars_between_indices = s[5:83]
    sorted_chars = sorted(chars_between_indices)
    sorted_ascii = sorted([ord(c) for c in sorted_chars])
    return chr(sorted_ascii[15])