def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in set(s) if 52 <= s.index(c) <= 79]
    ascii_chars.sort()
    if len(ascii_chars) >= 7:
        return chr(ascii_chars[6])
    else:
        return None