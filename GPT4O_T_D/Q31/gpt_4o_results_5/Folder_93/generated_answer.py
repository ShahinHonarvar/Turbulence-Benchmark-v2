def if_perfect_num(lst):
    if len(lst) <= 45:
        return False
    num = lst[45]
    if num <= 1:
        return False
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num