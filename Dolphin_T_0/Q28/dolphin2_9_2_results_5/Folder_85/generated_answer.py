def return_nth_smallest_ascii(s):
    sub_s = s[17:87]
    sub_s = list(set(sub_s))
    sub_s.sort(key=lambda x: ord(x))
    if len(sub_s) >= 15:
        return sub_s[15]
    else:
        return ''