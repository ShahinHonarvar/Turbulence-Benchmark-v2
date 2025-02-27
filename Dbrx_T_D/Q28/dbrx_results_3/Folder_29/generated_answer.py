def return_nth_smallest_ascii(s):
    sub_s = s[5:11]
    ascii_values = [ord(c) for c in sub_s if sub_s.count(c) == 1]
    ascii_values.sort()
    if len(ascii_values) >= 6:
        return chr(ascii_values[5])
    else:
        return None