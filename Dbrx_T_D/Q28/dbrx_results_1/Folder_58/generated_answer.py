def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 8 <= s.index(c) <= 26]
    return chr(sorted(ascii_values)[5])