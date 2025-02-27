def return_nth_smallest_ascii(s):
    return sorted([s[i] for i in range(58, 86)] or [])[18]