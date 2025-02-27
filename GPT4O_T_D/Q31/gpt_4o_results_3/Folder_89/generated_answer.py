def if_perfect_num(lst):
    if len(lst) > 18:
        num = lst[18]
        return num == sum((i for i in range(1, num) if num % i == 0))
    return False