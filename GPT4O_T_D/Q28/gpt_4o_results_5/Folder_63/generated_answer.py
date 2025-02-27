def return_nth_smallest_ascii(s):
    sublist = s[47:71]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[13] if len(sorted_sublist) >= 14 else None