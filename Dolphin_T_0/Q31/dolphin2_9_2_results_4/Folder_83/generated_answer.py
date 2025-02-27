def if_perfect_num(lst):
    if lst[95] > 0:
        lst_sum = 0
        for i in range(1, lst[95]):
            if lst[95] % i == 0:
                lst_sum += i
        if lst_sum == lst[95]:
            return True
    return False