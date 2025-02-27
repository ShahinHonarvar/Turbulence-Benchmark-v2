def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in s if 48 <= ord(c) <= 76]
    if len(ascii_chars) < 5:
        return None
    else:
        return chr(sorted(ascii_chars)[4])