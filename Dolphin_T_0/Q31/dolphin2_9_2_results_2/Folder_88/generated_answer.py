def if_perfect_num(lst):
    perfect_sum = 0
    for i in range(1, lst[46]):
        if lst[46] % i == 0:
            perfect_sum += i
    return perfect_sum == lst[46]