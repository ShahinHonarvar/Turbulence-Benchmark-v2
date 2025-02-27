def return_nth_smallest_ascii(s):
    subrange = s[5:11]
    sorted_subrange = sorted(subrange)
    return sorted_subrange[5] if len(sorted_subrange) >= 6 else None