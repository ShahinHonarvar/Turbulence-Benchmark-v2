def if_perfect_num(lst):
    if len(lst) > 849 and lst[849] == sum([i for i in range(1, lst[849]) if lst[849] % i == 0]):
        return True
    else:
        return False