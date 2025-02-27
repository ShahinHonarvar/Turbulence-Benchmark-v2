def if_perfect_num(lst):
    if sum([i for i in range(1, lst[42]) if lst[42] % i == 0]) == lst[42]:
        return True
    return False