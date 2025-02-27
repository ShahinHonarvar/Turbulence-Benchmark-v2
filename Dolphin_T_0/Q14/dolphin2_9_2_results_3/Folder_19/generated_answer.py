def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    elif len(lst) < 5:
        return min(lst[4:])
    else:
        s = sorted(lst[4:9])
        if s[1] != s[0]:
            return s[1]
        else:
            return None