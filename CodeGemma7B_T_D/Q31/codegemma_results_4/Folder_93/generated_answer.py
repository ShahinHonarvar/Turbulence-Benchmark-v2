def if_perfect_num(lst):
    if lst[45] == 1 or lst[45] == 0:
        return False
    sum = 0
    for i in range(1, lst[45]):
        if lst[45] % i == 0:
            sum += i
    return sum == lst[45]