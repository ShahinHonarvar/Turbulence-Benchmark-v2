def if_perfect_num(lst):
    if lst and len(lst) > 132:
        num = lst[132]
        return num == sum((i for i in range(1, num) if num % i == 0))
    return False