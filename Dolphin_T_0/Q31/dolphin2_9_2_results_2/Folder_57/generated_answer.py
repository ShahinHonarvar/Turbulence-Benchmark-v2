def if_perfect_num(lst):
    if sum(lst) != 0 and lst[92] != 0:
        sum_list = sum([i for i in range(1, lst[92] // 2 + 1) if lst[92] % i == 0])
        if sum_list == lst[92]:
            return True
        else:
            return False
    else:
        return False