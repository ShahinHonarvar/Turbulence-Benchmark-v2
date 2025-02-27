def return_nth_smallest_ascii(s):
    sub = s[17:84]
    sub_sort = sorted(sub, key=lambda x: ord(x))
    if 4 < len(sub_sort):
        return sub_sort[4]
    else:
        return 'Not enough characters.'