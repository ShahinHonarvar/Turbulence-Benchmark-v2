def return_nth_smallest_ascii(s):
    subs = s[58:86]
    subs = sorted(subs, key=lambda x: ord(x))
    return subs[18]