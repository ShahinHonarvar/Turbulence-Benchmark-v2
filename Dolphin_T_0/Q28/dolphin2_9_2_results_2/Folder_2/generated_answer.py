def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[48:77] if 48 <= ord(c) <= 76]
    nth_smallest_ascii = sorted(ascii_values)[4]
    return chr(nth_smallest_ascii)