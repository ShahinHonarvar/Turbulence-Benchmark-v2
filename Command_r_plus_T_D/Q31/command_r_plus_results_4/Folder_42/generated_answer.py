def if_perfect_num(lst):
    if len(lst) > 276 and lst[276] > 0:
        divisor_sum = sum([i for i in range(1, lst[276]) if lst[276] % i == 0])
        return divisor_sum == lst[276]
    return False