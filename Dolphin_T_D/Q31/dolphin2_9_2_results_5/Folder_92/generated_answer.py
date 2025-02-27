def if_perfect_num(lst):
    if lst[0] == 0:
        return False
    div_sum = 1
    for i in range(2, lst[0]):
        if lst[0] % i == 0:
            div_sum += i
    return div_sum == lst[0]