def if_perfect_num(lst):
    if lst[851] % sum([i for i in range(1, lst[851]) if lst[851] % i == 0]) == 0:
        return True
    else:
        return False