def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in s if 18 <= s.index(c) <= 66]
    if len(ascii_chars) >= 19:
        return chr(sorted(ascii_chars)[18])
    else:
        return None