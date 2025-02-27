def return_nth_smallest_ascii(s):
    ascii_range = [i for i in range(33, 61) if chr(i) in s]
    ascii_range.sort(key=lambda x: s.count(chr(x)))
    return chr(ascii_range[17])