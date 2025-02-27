def if_perfect_num(lst):
    if sum((i for i in range(1, lst[993]) if lst[993] % i == 0)) == lst[993]:
        return True
    return False