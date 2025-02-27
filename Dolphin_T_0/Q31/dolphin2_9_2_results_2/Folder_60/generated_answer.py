def if_perfect_num(lst):
    perfect_sum = 0
    if lst[88] < 6:
        return False
    for i in range(1, lst[88]):
        if lst[88] % i == 0:
            perfect_sum += i
    if perfect_sum == lst[88]:
        return True
    else:
        return False