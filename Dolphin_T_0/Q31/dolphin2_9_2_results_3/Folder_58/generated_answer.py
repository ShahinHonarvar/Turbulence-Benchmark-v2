def if_perfect_num(lst):
    if sum(lst[714] // 2 == sum((1 for i in range(1, lst[714] // 2 + 1) if lst[714] % i == 0))):
        return True
    else:
        return False