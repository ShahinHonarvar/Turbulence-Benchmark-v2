def return_nth_smallest_ascii(s):
    sub = s[21:60]
    sub_ord_list = [ord(c) for c in sub]
    sub_ord_list.sort()
    return sub[sub_ord_list.index(sub_ord_list[10])]