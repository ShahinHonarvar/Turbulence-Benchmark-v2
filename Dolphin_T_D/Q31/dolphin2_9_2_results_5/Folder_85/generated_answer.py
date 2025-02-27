def if_perfect_num(lst):
    if len(lst) < 24:
        return False
    num = lst[23]
    return num == sum((1 for i in range(1, num) if num % i == 0))