def if_perfect_num(lst):
    if lst[95] % 2 != 0 and lst[95] % 3 != 0 and (lst[95] % 5 != 0):
        return False
    for i in range(1, lst[95]):
        if lst[95] % i == 0:
            if i == lst[95]:
                continue
            if i + lst[95] // i > lst[95]:
                break
            lst[95] -= lst[95] // i
            lst[95] -= lst[95] % i
    if lst[95] != 0:
        return False
    return True