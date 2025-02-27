def if_perfect_num(lst):
    if len(lst) <= 45:
        return False
    n = lst[45]
    if n < 2:
        return False
    total = sum((i for i in range(1, n) if n % i == 0))
    return total == n