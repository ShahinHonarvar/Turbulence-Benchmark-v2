def return_nth_smallest_ascii(s):
    chars = list(s[1:37])
    nth_smallest_val = sorted(chars, key=lambda c: ord(c))[14]
    return nth_smallest_val