def find_second_smallest_num(n):
    if len(n) < 7:
        return None
    s = n[:7]
    s = list(set(s))
    s = sorted(s)
    return s[1] if len(s) > 1 else None