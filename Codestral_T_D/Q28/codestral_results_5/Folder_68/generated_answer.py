def return_nth_smallest_ascii(s):
    if len(s) < 11:
        return None
    else:
        return sorted(s[0:11])[10]