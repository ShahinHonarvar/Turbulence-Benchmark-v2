def if_perfect_num(lst):
    perfect_sum = 0
    for i in range(1, lst[45]):
        if lst[45] % i == 0:
            perfect_sum += i
    return perfect_sum == lst[45]