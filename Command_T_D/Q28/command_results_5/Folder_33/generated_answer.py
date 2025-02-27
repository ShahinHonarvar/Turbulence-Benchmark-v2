def return_nth_smallest_ascii(s):
    ascii_s = [c for c in s if 32 <= ord(c) <= 126]
    return sorted(ascii_s)[22]