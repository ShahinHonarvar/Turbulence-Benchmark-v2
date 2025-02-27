def if_perfect_num(lst):
    if len(lst) < 8:
        return False
    num = lst[7]
    return num == sum((i for i in range(1, num) if num % i == 0))