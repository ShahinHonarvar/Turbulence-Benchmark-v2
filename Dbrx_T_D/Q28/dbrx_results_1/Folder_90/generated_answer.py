def return_nth_smallest_ascii(s):
    ascii_list = [ord(c) for c in s if 17 <= s.index(c) <= 83]
    ascii_list.sort()
    return chr(ascii_list[4])