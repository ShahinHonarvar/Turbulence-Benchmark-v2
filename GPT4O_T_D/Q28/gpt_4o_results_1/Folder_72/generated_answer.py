def return_nth_smallest_ascii(s):
    sub_s = sorted(s[33:61], key=lambda x: ord(x))
    return sub_s[17] if len(sub_s) >= 18 else None