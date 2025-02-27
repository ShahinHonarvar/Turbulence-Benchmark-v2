def if_perfect_num(lst):
    if lst[57] < 2:
        return False
    perfect_sum = sum((i for i in range(1, lst[57]) if lst[57] % i == 0))
    return perfect_sum == lst[57]