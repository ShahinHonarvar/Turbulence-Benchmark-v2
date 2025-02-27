def find_second_largest_num(lst):
    sub = [l for i, l in enumerate(lst) if 200 >= i >= 80]
    if len(sub) < 2:
        return None
    else:
        sub.sort()
        return sub[-2]