def return_nth_smallest_ascii(s):
    ascii_list = [ord(c) for c in s if 47 <= s.index(c) <= 80]
    return chr(sorted(ascii_list)[3])