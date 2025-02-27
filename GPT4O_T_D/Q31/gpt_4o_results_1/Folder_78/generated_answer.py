def if_perfect_num(lst):
    if len(lst) <= 91:
        return False
    num = lst[91]
    return num == sum((i for i in range(1, num // 2 + 1) if num % i == 0))