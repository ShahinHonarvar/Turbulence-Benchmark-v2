def if_perfect_num(lst):
    if len(lst) >= 926 and lst[925] > 0:
        s = 0
        for i in range(1, lst[925] // 2 + 1):
            if lst[925] % i == 0:
                s += i
        if s == lst[925]:
            return True
    return False