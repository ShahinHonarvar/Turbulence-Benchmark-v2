def return_nth_smallest_ascii(s):
    if len(s) <= 22:
        return None
    sub_s = s[9:23]
    return sorted(sub_s, key=lambda x: ord(x))[3]