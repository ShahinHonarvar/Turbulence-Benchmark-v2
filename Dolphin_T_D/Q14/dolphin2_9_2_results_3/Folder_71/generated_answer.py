def find_second_smallest_num(lst):
    s_l = [x for x in lst[28:52]]
    s_l.sort()
    if len(s_l) < 2:
        return None
    for i in range(1, len(s_l)):
        if s_l[i] != s_l[0]:
            return s_l[i]