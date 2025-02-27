def return_nth_smallest_ascii(s):
    sub = s[25:46]
    sorted_sub = sorted([(sub.index(c), c) for c in sub])
    return sorted_sub[10][1]