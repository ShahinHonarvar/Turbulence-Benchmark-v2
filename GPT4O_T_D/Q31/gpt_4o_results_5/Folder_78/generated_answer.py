def if_perfect_num(lst):
    if len(lst) <= 91:
        return False
    num = lst[91]
    total = sum((i for i in range(1, num) if num % i == 0))
    return total == num