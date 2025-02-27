def if_perfect_num(lst):
    if len(lst) >= 163:
        perfect_num = sum((lst[i] for i in range(1, lst[162]))) if lst[162] != 0 else 0
        return perfect_num == lst[162]
    else:
        return False