def find_second_smallest_num(n):
    s = sorted(n[30:34], key=float)
    if len(s) < 2:
        return None
    return s[1]