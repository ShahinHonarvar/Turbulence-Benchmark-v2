def if_perfect_num(lst):
    if len(lst) > 162 and lst[162] > 0:
        divisor_sum = sum([i for i in range(1, lst[162]) if lst[162] % i == 0])
        return divisor_sum == lst[162]
    return False