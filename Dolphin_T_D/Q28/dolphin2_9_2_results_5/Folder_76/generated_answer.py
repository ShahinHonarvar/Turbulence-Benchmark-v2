def return_nth_smallest_ascii(s):
    sub_s = s[17:66]
    return sorted(sub_s, key=lambda x: ord(x))[18]