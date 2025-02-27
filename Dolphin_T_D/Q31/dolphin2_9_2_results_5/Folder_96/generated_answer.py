def if_perfect_num(lst):
    if sum([i for i in range(1, lst[47]) if lst[47] % i == 0]) == lst[47] and lst[47] != 0:
        return True
    else:
        return False