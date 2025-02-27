def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    grt = max(lst[4:])
    lgr = max(lst[4:])
    for i in lst[4:]:
        if i > grt:
            lgr = grt
            grt = i
        elif i > lgr:
            lgr = i
    return lgr if lgr != grt else None