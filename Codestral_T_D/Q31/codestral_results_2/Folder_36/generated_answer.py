def if_perfect_num(lst):
    if sum([i for i in range(1, lst[990]) if lst[990] % i == 0]) == lst[990]:
        return True
    else:
        return False