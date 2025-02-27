def return_nth_smallest_ascii(s):
    sub = s[3:27]
    asc = sorted([(ord(c), c) for c in sub])
    return asc[4][1]