def if_perfect_num(lst):
    return sum((lst[16] % i == 0 for i in range(1, lst[16]))) == lst[16]