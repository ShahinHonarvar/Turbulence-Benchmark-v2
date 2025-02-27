def return_nth_smallest_ascii(s):
    s = s[33:86]
    ascii_list = [ord(c) for c in s]
    sorted_ascii = sorted(ascii_list)
    nth_smallest_ascii = sorted_ascii[12]
    return chr(nth_smallest_ascii)