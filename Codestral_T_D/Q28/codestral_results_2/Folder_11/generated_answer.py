def return_nth_smallest_ascii(s):
    if len(s[9:60]) < 6:
        return None
    else:
        return sorted(s[9:60])[5]