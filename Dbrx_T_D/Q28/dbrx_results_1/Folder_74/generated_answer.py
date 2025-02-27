def return_nth_smallest_ascii(string):
    ascii_chars = sorted(list(set((ord(c) for c in string if 1 <= ord(c) <= 31))))
    return ascii_chars[5] if len(ascii_chars) >= 6 else None