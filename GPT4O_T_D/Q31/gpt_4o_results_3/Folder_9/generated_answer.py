def if_perfect_num(lst):
    if len(lst) <= 24:
        return False
    num = lst[24]
    return sum((i for i in range(1, num) if num % i == 0)) == num